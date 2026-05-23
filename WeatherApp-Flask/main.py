from flask import Flask

app = Flask(__name__)

@app.route("/")
def HomePage():
    return "<p>Weather App</p>"

if __name__ == "__main__":
    app.run(debug=True)