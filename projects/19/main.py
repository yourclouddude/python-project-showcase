"""Local form app: escaped HTML preview and in-memory PDF download."""
from decimal import Decimal, InvalidOperation
from html import escape
from io import BytesIO
from pathlib import Path
from uuid import uuid4
from fastapi import FastAPI, Form, HTTPException
from fastapi.responses import HTMLResponse, Response
from jinja2 import Environment, FileSystemLoader, select_autoescape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle

app = FastAPI()
templates = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"), autoescape=select_autoescape(["html"]))

def invoice_data(client, service, quantity, rate):
    if not client.strip() or not service.strip() or len(client) > 120 or len(service) > 500 or not 1 <= quantity <= 10000:
        raise ValueError("Client/service and quantity are invalid.")
    try:
        price = Decimal(str(rate))
        if not price.is_finite() or price < 0 or price > 1_000_000 or price.as_tuple().exponent < -2:
            raise ValueError("Rate must be finite, nonnegative and have at most two decimal places.")
    except InvalidOperation as error:
        raise ValueError("Enter a valid rate.") from error
    return {"client": client.strip(), "service": service.strip(), "quantity": quantity, "rate": f"{price:.2f}", "total": f"{price * quantity:.2f}", "invoice_id": str(uuid4())}

def make_pdf(data):
    buffer = BytesIO()
    styles = getSampleStyleSheet()
    story = [Paragraph("INVOICE", styles["Title"]), Paragraph(escape(data["invoice_id"]), styles["Normal"]), Spacer(1, 18), Paragraph("Client: " + escape(data["client"]), styles["Normal"]), Spacer(1, 18)]
    table = Table([["Service", "Quantity", "Rate (USD)", "Total (USD)"], [Paragraph(escape(data["service"]), styles["Normal"]), str(data["quantity"]), data["rate"], data["total"]]], colWidths=[245, 60, 90, 90], repeatRows=1)
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#e7eef9")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("GRID", (0, 0), (-1, -1), .4, colors.lightgrey), ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]))
    story.extend([table, Spacer(1, 18), Paragraph("Learning demo. Tax, payment collection and legal invoice requirements are outside this core.", styles["Normal"])])
    SimpleDocTemplate(buffer, title="Invoice", leftMargin=42, rightMargin=42).build(story)
    return buffer.getvalue()

@app.get("/", response_class=HTMLResponse)
def index():
    return templates.get_template("invoice.html").render(data=None)

@app.post("/generate")
def generate(client: str = Form(...), service: str = Form(...), quantity: int = Form(...), rate: str = Form(...), preview: bool = Form(False)):
    try:
        data = invoice_data(client, service, quantity, rate)
    except ValueError as error:
        raise HTTPException(422, str(error)) from error
    if preview:
        return HTMLResponse(templates.get_template("invoice.html").render(data=data))
    return Response(make_pdf(data), media_type="application/pdf", headers={"Content-Disposition": 'attachment; filename="invoice.pdf"'})
