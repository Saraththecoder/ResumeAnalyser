from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        hours = float(request.form["hours"])
        prediction = model.predict(np.array([[hours]]))
        predicted_marks = round(prediction[0], 2)

        return render_template(
            "result.html",
            hours=hours,
            marks=predicted_marks
        )

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
