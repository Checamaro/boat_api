from flask import Flask, render_template
import requests

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/status")
def status():
    response = requests.get("http://127.0.0.1:5000/status")
    boat_data = response.json()
    return render_template("boat_status.html", boat=boat_data)

if __name__ == "__main__":
    app.run(debug=True, port=8001)

