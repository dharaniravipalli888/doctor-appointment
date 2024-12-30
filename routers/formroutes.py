from flask import Blueprint, render_template, request, redirect, url_for
from models.formmodels import Application

# Create a Blueprint for handling the form
form_blueprint = Blueprint('form', __name__)

# Route to show the application form
@form_blueprint.route("/apply", methods=["GET", "POST"])
def apply():
    if request.method == "POST":
        # Retrieve data from the form
        name = request.form["name"]
        age = request.form["age"]
        date = request.form["date"]
        phone_number = request.form["phone_number"]
        issue = request.form["issue"]
        time = request.form["time"]
        doctor_name = request.form["doctor_name"]
        
        # Create an Application object and save to MongoDB
        application = Application(name, age, date, phone_number, issue, time, doctor_name)
        application.save_to_db()

        # Redirect to the thank you page
        return redirect(url_for("form.thank_you"))

    return render_template("form.html")

# Route for the thank you page
@form_blueprint.route('/thank-you')
def thank_you():
    return "<h1>Thank you for applying! We will contact you shortly.</h1>"
