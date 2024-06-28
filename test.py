from flask import Flask, render_template, redirect, url_for,request
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(
  
    api_key=os.environ.get("OPENAI_API_KEY"))
MODEL = 'gpt-4o'

@app.route("/", methods=("GET", "POST"))
def index():
  if request.method == "POST":
    message = request.form["message"]
    response = client.chat.completions.create(
      model=MODEL,
      messages=[{"role": "user", "content": message}],
      temperature=0
    )
    result = response.choices[0].message.content.strip()
    return redirect(url_for("index", result=result))

  result = request.args.get("result")
  return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)

