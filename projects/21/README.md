# Dev Portfolio Generator

Generate a responsive, accessible static portfolio from validated profile.json using Jinja2 autoescape and deliberate output creation.

## Implemented core
- Checks required strings, project records and HTTPS links.
- Loads a source-relative template, enables autoescape, creates output directories and requires explicit overwrite.
- Uses a viewport tag, semantic landmarks, keyboard focus styling and a responsive project grid.

## Setup and run
From projects/21/ in this repository. Use Python 3.12 and a separate environment.

    python -m venv .venv
    # PowerShell
    .\.venv\Scripts\Activate.ps1
    # macOS/Linux alternative
    source .venv/bin/activate
    python -m pip install -r requirements.txt

    python generate.py

## Expected result
Creates output/index.html. Open the file locally; sample project link uses example.com as a deliberate placeholder.

## Important failure check
Missing profile fields and javascript links are rejected; existing output is preserved unless --overwrite is explicit.

## Optional extension
Add a skills/contact section with URL validation, another theme and an automated accessibility/build check.

## Learning evidence
Explain: Why does HTML escaping alone not make an arbitrary link safe? Add one original requirement, a sample artifact and a short decision/test log. Credit any assistance and distinguish the supplied core from your own work.

## Boundaries and verification
For GitHub Pages, publish the generated file at an allowed source: copy output/index.html to the repository root, commit it to your chosen branch, then Settings → Pages → Deploy from a branch → that branch → /(root). A raw /output folder is not the branch-source setting. The generated page can also be copied to /docs and published from /docs. Hosting/account steps are instructions only; no site is deployed. Replace placeholder URLs with your actual verified project links.

Runtime checked: Windows x64, Python 3.12.14, 8 October 2026. This project passed a clean dependency installation and an offline smoke scenario in its own environment; the selected-project regression suite is included at the repository root. The complete vault previously passed 52 regression checks. Other OS/Python and live-account branches are not verified. Use the README commands from the source folder, not a generic filename copied from another lesson.

## Official reference
[GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site)
