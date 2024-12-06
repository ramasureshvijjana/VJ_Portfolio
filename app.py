from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    # Load data if required, or just render the projects template
    return render_template("index.html")


@app.route("/projects")
def projects():

    # Load data from Excel
    data = pd.read_excel("projects.xlsx")

    # Convert rows to a list of dictionaries for easy iteration in the template
    projects = data.to_dict(orient="records")
    
    return render_template("projects.html", projects=projects)


if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0')
