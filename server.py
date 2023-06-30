"""
A server file for SILVERSTONE CONTRACTING & Landscaping 
"""
import os
from datetime import datetime
from flask import Flask, render_template, redirect, request, flash, session
import jinja2
from emailme import send_an_email

# from model import db
# from model import Routine, User, Exercise, PracticeSession, db
# from crud import last_two_sessions, get_user_by_id
# from datetime import datetime

app = Flask(__name__)
app.secret_key = 's0m3TH!ng'
PASSWORD = os.environ['SMTPPASSWORD']
# print(PASSWORD)

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

@app.route("/contact", methods=["GET", "POST"])
def contact():
    """Return contact page."""

    if request.method == 'POST':
        time = datetime.now()
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]
        service = request.form["services"]
        message_body = request.form["message-body"]

        client_message = """\
        Message Sent: {time}\n
        Client Name: {name}\n
        Client Email: {email}\n
        Client Phone: {phone}\n
        Services Requested: {service}\n
        More Details: {message_body}""".format(time=time, name=name, email=email, phone=phone, service=service, message_body=message_body)

        send_an_email(password=PASSWORD, msg=client_message)
        flash("email sent")
        return render_template("contact.html")

    elif request.method == 'GET':
        return render_template("contact.html")

@app.route("/contacts", methods=["GET", "POST"])
def contacts():
    """Return contact page."""
    form = ContactForm()
    if request.method == 'POST':
        if not form.validate():
            flash('All fields are required.')
            return render_template('contacts.html', form=form, success=False)
        else:
            msg = Message("Silverstone Web Form Request", sender='justferfunan@gmail.com', recipients=['justferfunan@gmail.com'])
            msg.body = f"From: {form.name.data} <{form.email.data}>\n{form.message.data}"
            mail.send(msg)
            return render_template("contacts.html", form=form, success=True)
    elif request.method == 'GET':
        return render_template("contacts.html", form=form, success=False)



if __name__ == "__main__":
    # from model import connect_to_db
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)