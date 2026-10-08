from pathlib import Path
from io import BytesIO
import importlib.util
import json
import pytest
from fastapi.testclient import TestClient
from pypdf import PdfReader

ROOT=Path(__file__).parent
FILES={21:'generate.py'}
def load(i,filename=None):
    path=ROOT/'projects'/f'{i:02}'/(filename or FILES.get(i,'main.py'))
    spec=importlib.util.spec_from_file_location(f'project_{i}_{path.stem}',path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module
def fixture(i,name):
    return ROOT/'projects'/f'{i:02}'/name

@pytest.mark.parametrize('value',['nan','inf','-1','1.001'])
def test_expense_amounts(value):
    with pytest.raises(ValueError): load(6).money(value)

def test_expense_csv(tmp_path):
    m=load(6); totals,errors=m.summarize(fixture(6,'sample_expenses.csv'))
    assert str(sum(totals.values()))=='19.75' and errors==[4]
    path=tmp_path/'expenses.csv'; m.add_expense(path,'2.50','Food'); assert str(m.summarize(path)[0]['Food'])=='2.50'

def test_book_api_identity_and_persistence(tmp_path,monkeypatch):
    monkeypatch.setenv('BOOKS_DB',str(tmp_path/'global.db')); m=load(13)
    database=tmp_path/'books.db'; client=TestClient(m.create_app(database))
    book=json.loads(fixture(13,'sample_book.json').read_text())
    a=client.post('/books',json=book); b=client.post('/books',json=book)
    assert a.status_code==201 and b.json()['id']!=a.json()['id'] and a.json()['available'] is True
    assert client.put('/books/1',json=book|{'id':99}).status_code==422
    assert client.post('/books',json=book|{'price':'-1'}).status_code==422
    assert TestClient(m.create_app(database)).get('/books/1').json()['price']=='12.50'
    assert client.delete('/books/1').status_code==204 and client.get('/books/1').status_code==404

def test_invoice_pdf_and_validation():
    m=load(19); data=m.invoice_data('Sample Client','API prototype',2,'125.50')
    assert data['total']=='251.00'
    pdf=m.make_pdf(data); assert '251.00' in PdfReader(BytesIO(pdf)).pages[0].extract_text()
    client=TestClient(m.app)
    assert client.get('/').status_code==200
    assert client.post('/generate',data={'client':'C','service':'S','quantity':'2','rate':'-1'}).status_code==422
    response=client.post('/generate',data={'client':'<script>','service':'S','quantity':'2','rate':'3.50','preview':'true'})
    assert '&lt;script&gt;' in response.text
    assert client.post('/generate',data={'client':'C','service':'S','quantity':'2','rate':'3.50'}).content.startswith(b'%PDF')

@pytest.mark.parametrize('rate',['nan','inf','-2','1.001'])
def test_invoice_invalid(rate):
    with pytest.raises(ValueError): load(19).invoice_data('C','S',1,rate)

def test_portfolio_escape_and_output(tmp_path):
    m=load(21); data=json.loads(fixture(21,'profile.json').read_text()); data['name']='<script>alert(1)</script>'
    source=tmp_path/'profile.json'; source.write_text(json.dumps(data)); target=m.generate(source,tmp_path/'output')
    assert '&lt;script&gt;' in target.read_text()
    with pytest.raises(FileExistsError): m.generate(source,tmp_path/'output')
    data['projects'][0]['url']='javascript:alert(1)'
    with pytest.raises(ValueError): m.validate(data)
