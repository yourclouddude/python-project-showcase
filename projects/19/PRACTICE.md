# Practice — Invoice Generator Web App

**Readiness check:** Why should HTML and PDF use one validated total?
**Check your answer:** Two independent calculations can disagree. Validate and calculate once, then render the same values.
**Your first build:** `invoice_total(quantity, rate)` — Require integer quantity 1–10,000 (not bool) and finite Decimal-compatible rate 0–1,000,000 with at most two decimal places. Return a two-place total string; invalid input raises ValueError. No renderer or file write.
This is a bounded learning helper, not a drop-in replacement for the full app. Keep the original source available for comparison.
```python
def invoice_total(quantity, rate):
    """Require integer quantity 1–10,000 (not bool) and finite Decimal-compatible rate 0–1,000,000 with at most two decimal places. Return a two-place total string; invalid input raises ValueError. No renderer or file write."""
    # Implement the contract; keep the complete project source unchanged.
    raise NotImplementedError("Your practice implementation goes here.")
```
**Try before looking:** predict one valid result and one rejection; write the helper in `practice_starter.py`, then run `python practice_checks.py` from this project folder. The untouched starter intentionally fails; use the test name and assertion to locate the missing behavior. These five checks sample the contract; they do not prove every possible input correct.
**Hint 1:** Parse the entered rate as Decimal.
**Hint 2:** Reject precision before multiplying.
**Compare after an attempt:** `practice_reference.py` contains a separate worked answer. Run `python practice_checks.py --reference`, then explain one difference without copying it back blindly. The full original project remains in its existing source files.
**Debugging exercise:** Changing HTML CSS does not change the PDF. What is the actual rendering path?
**Feedback — read after predicting:** Jinja2 renders HTML; ReportLab builds the PDF separately. Verify approved values in both artifacts; CSS is not a shared layout engine.
**Independent extension:** Add multiple line items. **Acceptance evidence:** Line totals sum exactly; HTML/PDF show the same quantity, rates and total; long content paginates.
**Completion standard:** show the original sample result, passing checks for your own helper, one explained failure, and a short decision log. Describe supplied code, your changes and any assistance accurately. Passing only the worked answer checks does not demonstrate your mastery.
**Return to it:** next day, explain the validation boundary without the solution; after one week, rebuild the helper and one failure check. These are suggested revision intervals, not scheduled reminders.
