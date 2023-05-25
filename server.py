"""
A server file for SILVERSTONE CONTRACTING & Landscaping 
"""
from model import db
from flask import Flask, render_template, redirect, request, flash, session
import jinja2
# from model import Routine, User, Exercise, PracticeSession, db
# from crud import last_two_sessions, get_user_by_id
# from datetime import datetime

app = Flask(__name__)
app.secret_key = 's0m3TH!ng'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.
app.jinja_env.undefined = jinja2.StrictUndefined

# This configuration option makes the Flask interactive debugger
# more useful (you should remove this line in production though)
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True


@app.route("/")
def landing():
    """Return homepage."""

    return render_template("landing.html")

@app.route("/about")
def about():
    """Return about page."""

    return render_template("about.html")

@app.route("/services")
def services():
    """Return services page."""

    return render_template("services.html")

@app.route("/projects")
def projects():
    """Return projects page."""

    return render_template("projects.html")

@app.route("/contact")
def contact():
    """Return contact page."""

    return render_template("contact.html")



if __name__ == "__main__":
    # from model import connect_to_db
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)