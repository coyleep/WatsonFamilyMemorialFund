import os
from flask import Flask, render_template, request

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response



@app.route("/")
def hompage():
    return render_template("homepage.html")

@app.route("/about")
def aboutUs():
    return render_template("about.html")

@app.route("/Events")
def education():
    return render_template("events.html")





if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)