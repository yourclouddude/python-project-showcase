# Practice — Expense Tracker (CSV)

**Readiness check:** Why parse money from text rather than a float?
**Check your answer:** A binary float may already contain rounding error. Decimal from the original text preserves the entered decimal value.
**Your first build:** `money(text)` — Parse via Decimal(str(text)); require finite, nonnegative values with at most two decimal places. Return Decimal quantized to 0.01. Invalid values raise ValueError; malformed Decimal input may raise InvalidOperation.
This is a bounded learning helper, not a drop-in replacement for the full app. Keep the original source available for comparison.
```python
def money(text):
    """Parse via Decimal(str(text)); require finite, nonnegative values with at most two decimal places. Return Decimal quantized to 0.01. Invalid values raise ValueError; malformed Decimal input may raise InvalidOperation."""
    # Implement the contract; keep the complete project source unchanged.
    raise NotImplementedError("Your practice implementation goes here.")
```
**Try before looking:** predict one valid result and one rejection; write the helper in `practice_starter.py`, then run `python practice_checks.py` from this project folder. The untouched starter intentionally fails; use the test name and assertion to locate the missing behavior. These five checks sample the contract; they do not prove every possible input correct.
**Hint 1:** Check is_finite before comparisons.
**Hint 2:** Check exponent before quantizing so excess precision is rejected.
**Compare after an attempt:** `practice_reference.py` contains a separate worked answer. Run `python practice_checks.py --reference`, then explain one difference without copying it back blindly. The full original project remains in its existing source files.
**Debugging exercise:** A CSV total is plausible but line 4 contains NaN. What evidence is missing?
**Feedback — read after predicting:** Reject and report the row by line number; report valid-row total separately. A plausible sum does not prove every row was accepted.
**Independent extension:** Add monthly category budgets. **Acceptance evidence:** YYYY-MM filtering is exact; show remaining/overspent amounts and a malformed-row report.
**Completion standard:** show the original sample result, passing checks for your own helper, one explained failure, and a short decision log. Describe supplied code, your changes and any assistance accurately. Passing only the worked answer checks does not demonstrate your mastery.
**Return to it:** next day, explain the validation boundary without the solution; after one week, rebuild the helper and one failure check. These are suggested revision intervals, not scheduled reminders.
