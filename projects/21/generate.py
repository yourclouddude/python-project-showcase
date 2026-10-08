"""Generate escaped static HTML from validated portfolio JSON."""
import argparse
import json
from pathlib import Path
from urllib.parse import urlparse
from jinja2 import Environment, FileSystemLoader, select_autoescape

def validate(data):
    for key in ("name", "headline", "about"):
        if not isinstance(data.get(key), str) or not data[key].strip():
            raise ValueError(f"Missing {key}.")
    if not isinstance(data.get("projects"), list):
        raise ValueError("projects must be a list.")
    for project in data["projects"]:
        if not isinstance(project, dict) or not all(isinstance(project.get(key), str) and project[key].strip() for key in ("title", "description", "url")):
            raise ValueError("Every project needs title,description,url.")
        link = urlparse(project["url"])
        if link.scheme != "https" or not link.netloc:
            raise ValueError("Project links must use HTTPS.")
    return data

def generate(source, output, overwrite=False):
    data = validate(json.loads(Path(source).read_text(encoding="utf-8")))
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"), autoescape=select_autoescape(["html"]))
    html = env.get_template("index_template.html").render(**data)
    folder = Path(output)
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / "index.html"
    with target.open("w" if overwrite else "x", encoding="utf-8") as file:
        file.write(html)
    return target

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="profile.json")
    parser.add_argument("--output", default="output")
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    try:
        print(generate(args.data, args.output, args.overwrite))
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")

if __name__ == "__main__":
    main()
