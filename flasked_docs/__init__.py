import os

import markdown
from flask import Blueprint, abort, redirect, render_template, url_for

bp = Blueprint(
    "flasked_docs", __name__, template_folder="templates", static_folder="static"
)


@bp.route("/")
@bp.route("/<path:path>")
def doc(path="index"):
    # If the path ends with index.md, redirect to the path without index.md
    if path.endswith("index.md"):
        return redirect(url_for("flasked_docs.doc", path=path[:-8]))

    # If the path ends with .md, redirect to the path without .md
    if path.endswith(".md"):
        return redirect(url_for("flasked_docs.doc", path=path[:-3]))

    # If the path is empty string or ends with slash, set path to the index.md in the path
    if path == "" or path == "index.md" or path == "index":
        path = "index.md"

    if path.endswith("/"):
        path = f"{path}index.md"

    path = "docs/" + path

    if not path.endswith(".md"):
        path += ".md"

    if not os.path.exists(path):
        abort(404)

    return render_template("flasked_docs/base.html", html=markdown_to_html(path))


def markdown_to_html(path):
    """Convert a markdown file to HTML."""
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    return markdown.markdown(
        text,
        extensions=[
            "markdown.extensions.tables",
            "markdown.extensions.fenced_code",
            "markdown.extensions.codehilite",
            "markdown.extensions.toc",
            "markdown.extensions.meta",
        ],
    )


class FlaskedDocs:
    def __init__(self, app=None, docs_path="docs", url_prefix="/docs"):
        self.app = app
        self.docs_path = docs_path
        self.url_prefix = url_prefix

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.app = app
        app.register_blueprint(bp, url_prefix=self.url_prefix)
