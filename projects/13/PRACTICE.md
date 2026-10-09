# Practice — Bookstore REST API

**Readiness check:** Who assigns the id of a newly created book?
**Check your answer:** The server/database; the client sends validated book fields, not its chosen server id.
**Your first build:** `validate_book(payload)` — Validate title/author (1–120 chars, nonblank), Decimal price (0+, at most 10 digits and 2 decimal places), available Boolean default True, and no extra fields. Return trimmed strings and a two-place price string. No database operation.
This is a bounded learning helper, not a drop-in replacement for the full app. Keep the original source available for comparison.
```python
def validate_book(payload):
    """Validate title/author (1–120 chars, nonblank), Decimal price (0+, at most 10 digits and 2 decimal places), available Boolean default True, and no extra fields. Return trimmed strings and a two-place price string. No database operation."""
    # Implement the contract; keep the complete project source unchanged.
    raise NotImplementedError("Your practice implementation goes here.")
```
**Try before looking:** predict one valid result and one rejection; write the helper in `practice_starter.py`, then run `python practice_checks.py` from this project folder. The untouched starter intentionally fails; use the test name and assertion to locate the missing behavior. These five checks sample the contract; they do not prove every possible input correct.
**Hint 1:** Use a model that forbids extra fields.
**Hint 2:** Normalize the returned representation after validation.
**Compare after an attempt:** `practice_reference.py` contains a separate worked answer. Run `python practice_checks.py --reference`, then explain one difference without copying it back blindly. The full original project remains in its existing source files.
**Debugging exercise:** A malformed price returns 404. What is confused?
**Feedback — read after predicting:** Request schema failure is 422; a valid path id with no record is 404. Persistence after restart requires a file-backed database.
**Independent extension:** Add pagination. **Acceptance evidence:** Validate bounds; ordering is stable; adjacent pages have no repeated ids on a fixed dataset.
**Completion standard:** show the original sample result, passing checks for your own helper, one explained failure, and a short decision log. Describe supplied code, your changes and any assistance accurately. Passing only the worked answer checks does not demonstrate your mastery.
**Return to it:** next day, explain the validation boundary without the solution; after one week, rebuild the helper and one failure check. These are suggested revision intervals, not scheduled reminders.
