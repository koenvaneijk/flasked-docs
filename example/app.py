from flask import Flask

from flasked_docs import FlaskedDocs

app = Flask(__name__)

flasked_docs = FlaskedDocs(app)

if __name__ == "__main__":
    app.run(debug=True)  # Don't do this in production
