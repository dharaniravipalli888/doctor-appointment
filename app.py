from flask import Flask, redirect, url_for
from routers.routers import auth  # Import the auth blueprint
from routers.formroutes import form_blueprint
# Initialize Flask app
app = Flask(__name__)
app.secret_key = "your_secret_key"

# Register Blueprint
app.register_blueprint(auth)
app.register_blueprint(form_blueprint)


@app.route("/")
def home():
    # Redirect to the login page as the default page
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(debug=True)
