"""Decimal amounts, UTF-8 CSV and corrupt-row reporting."""
import argparse
import csv
from datetime import date
from decimal import Decimal, InvalidOperation
from pathlib import Path

HEADER = ["date", "amount", "category", "note"]

def money(text):
    value = Decimal(str(text))
    if not value.is_finite() or value < 0 or value.as_tuple().exponent < -2:
        raise ValueError("Use a non-negative finite amount with at most two decimal places.")
    return value.quantize(Decimal("0.01"))

def add_expense(path, amount, category, note=""):
    value = money(amount)
    if not category.strip():
        raise ValueError("Category is required.")
    path = Path(path)
    new = not path.exists() or path.stat().st_size == 0
    with path.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        if new:
            writer.writerow(HEADER)
        writer.writerow([date.today().isoformat(), str(value), category.strip(), note])

def summarize(path, month=None):
    totals, errors = {}, []
    with Path(path).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames != HEADER:
            raise ValueError("CSV header must be date,amount,category,note.")
        for line, row in enumerate(reader, 2):
            try:
                date.fromisoformat(row["date"])
                value = money(row["amount"])
                category = row["category"].strip()
                if not category or None in row or row["note"] is None:
                    raise ValueError("Missing or extra fields.")
                if month is None or row["date"].startswith(month):
                    totals[category] = totals.get(category, Decimal("0.00")) + value
            except (ValueError, InvalidOperation, TypeError, AttributeError):
                errors.append(line)
    return totals, errors

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default="expenses.csv")
    parser.add_argument("--add", nargs=2, metavar=("AMOUNT", "CATEGORY"))
    parser.add_argument("--month", help="YYYY-MM filter")
    args = parser.parse_args()
    try:
        if args.add:
            add_expense(args.file, *args.add)
        totals, errors = summarize(args.file, args.month)
        for category, total in totals.items():
            print(category, total)
        print("Total:", sum(totals.values(), Decimal("0.00")), "| Invalid rows skipped:", errors)
    except (OSError, ValueError, InvalidOperation) as error:
        print("Expense operation failed:", error)

if __name__ == "__main__":
    main()
