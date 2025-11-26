from flask import Flask, render_template, request, jsonify
from skills import extract_skills

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    top_skills = None
    resume_text = ""

    if request.method == "POST":
        resume_text = request.form.get("resume")
        top_skills = extract_skills(resume_text)

    return render_template("index.html", top_skills=top_skills, resume_text=resume_text)


# ------------------------------
# NEW API ENDPOINT
# ------------------------------
@app.route("/api/extract_skills", methods=["POST"])
def api_extract_skills():
    resume_text = request.data.decode("utf-8")  # Read plain text body

    top_skills = extract_skills(resume_text)

    return ", ".join(top_skills)  # Return plain text



if __name__ == "__main__":
    app.run(debug=True)

