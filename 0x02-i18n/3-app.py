#!/usr/bin/env python3
"""A Basic Flask app with internationalization support."""
from flask import Flask, render_template, request
from flask_babel import Babel
from jinja2 import select_autoescape

class Config:
    """Represents a Flask Babel configuration."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

# Enable autoescaping in Jinja2 templates
app.jinja_env.autoescape = select_autoescape(['html', 'xml'])


def get_locale() -> str:
    """Determines the best match with supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])

babel.locale_selector_func = get_locale


@app.route('/')
def index() -> str:
    """The home page."""
    return render_template('3-index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

