from flask import Flask

app = Flask(__name__)

app.config["SECRET_KEY"] = "change-this-secret-key"


@app.route("/")
def home():
    return """
    <h1>AI Smart Waste Management System</h1>
    <p>System is running successfully.</p>
    <p>Version 1 - Backend Started</p>
    """


if __name__ == "__main__":
    app.run(debug=True)