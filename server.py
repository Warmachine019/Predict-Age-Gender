from flask import Flask, render_template, request
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    current_year = datetime.now().year

    if request.method == "POST":
        name = request.form.get("username", "").strip()
        if name:
            try:
                response1 = requests.get(f"https://api.genderize.io/?name={name}")
                response2 = requests.get(f"https://api.agify.io?name={name}")
                gender = response1.json().get("gender", "Unknown")
                age = response2.json().get("age", "Unknown")
                return render_template("index.html", username=name, gender=gender, age=age, year=current_year)
            except Exception as e:
                return render_template("default.html", year=current_year, error="API error occurred.")
        else:
            return render_template("default.html", year=current_year, error="Please enter a name.")

    return render_template("default.html", year=current_year)

if __name__ == "__main__":
    app.run(debug=True)