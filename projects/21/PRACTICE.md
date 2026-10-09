# Practice — Dev Portfolio Generator

**Readiness check:** Does HTML escaping make a javascript: link safe?
**Check your answer:** No. Escaping prevents markup interpretation; URL-scheme validation is a separate check.
**Your first build:** `validate_profile(data)` — Require nonblank name/headline/about strings and a projects list. Each project needs title, description and an absolute HTTPS url. Return data unchanged; invalid fields raise ValueError. HTML escaping remains a separate renderer responsibility.
This is a bounded learning helper, not a drop-in replacement for the full app. Keep the original source available for comparison.
```python
def validate_profile(data):
    """Require nonblank name/headline/about strings and a projects list. Each project needs title, description and an absolute HTTPS url. Return data unchanged; invalid fields raise ValueError. HTML escaping remains a separate renderer responsibility."""
    # Implement the contract; keep the complete project source unchanged.
    raise NotImplementedError("Your practice implementation goes here.")
```
**Try before looking:** predict one valid result and one rejection; write the helper in `practice_starter.py`, then run `python practice_checks.py` from this project folder. The untouched starter intentionally fails; use the test name and assertion to locate the missing behavior. These five checks sample the contract; they do not prove every possible input correct.
**Hint 1:** Validate project records one at a time.
**Hint 2:** Parse URL scheme and host.
**Compare after an attempt:** `practice_reference.py` contains a separate worked answer. Run `python practice_checks.py --reference`, then explain one difference without copying it back blindly. The full original project remains in its existing source files.
**Debugging exercise:** A profile containing <script> is validated as text. Is it safe to render raw?
**Feedback — read after predicting:** No. Render with autoescape as well as validated URL schemes. Confirm keyboard navigation and published placeholder links separately.
**Independent extension:** Add a skills/contact section and second theme. **Acceptance evidence:** No arbitrary scripts or unsafe URL schemes; check mobile layout, keyboard focus and verified links.
**Completion standard:** show the original sample result, passing checks for your own helper, one explained failure, and a short decision log. Describe supplied code, your changes and any assistance accurately. Passing only the worked answer checks does not demonstrate your mastery.
**Return to it:** next day, explain the validation boundary without the solution; after one week, rebuild the helper and one failure check. These are suggested revision intervals, not scheduled reminders.
