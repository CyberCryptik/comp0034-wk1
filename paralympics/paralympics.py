from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the Paralympics app!"


# Add a route that accepts a name as a variable
@app.route("/hello/<name>")
def hello_name(name):
    # Use the name variable to create a personalized message
    return f"Hello {name}, welcome to my Paralympics app!"


if __name__ == "__main__":
    app.run(debug=True)
