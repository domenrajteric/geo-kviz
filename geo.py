
from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Dictionary with countries and their capitals
countries_cities = {
    "Slovenia": "Ljubljana",
    "Austria": "Vienna",
    "Croatia": "Zagreb",
    "Italy": "Rome",
    "Hungary": "Budapest",
    "Belgium": "Brussels",
    "Bulgaria": "Sofia",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Estonia": "Tallinn",
    "Finland": "Helsinki",
    "France": "Paris",
    "Germany": "Berlin",
    "Greece": "Athens",
    "Ireland": "Dublin",
    "Latvia": "Riga",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg City",
    "Malta": "Valletta",
    "Netherlands": "Amsterdam",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Romania": "Bucharest",
    "Slovakia": "Bratislava",
    "Spain": "Madrid",
    "Sweden": "Stockholm"
}

@app.route("/", methods=["GET", "POST"])
def index():

    feedback = None

    # Receive data from user
    if request.method == "POST":
        answer = request.form.get("answer")
        correct_answer = request.form.get("correct_answer")

        if answer.strip().lower() == correct_answer.lower():
            feedback = "Correct!"
        else:
            feedback = f"Wrong, correct answer was {correct_answer}!"

    # QUIZ
    # Choose a random country (KEY) from the dictionary
    country = random.choice(list(countries_cities.keys()))

    # Get the matching value (capital city)
    capital = countries_cities[country]

    question = f"What is the capital city of {country}?"

    return render_template("index.html", question=question, correct_answer=capital, feedback=feedback)


if __name__ == "__main__":
    app.run()