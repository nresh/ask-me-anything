import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        query = request.form["query"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=query,
            temperature=0.6,
            n=1,
            max_tokens=1000,
        )
        print(response.choices)
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)
