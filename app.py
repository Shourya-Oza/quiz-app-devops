from flask import Flask, request, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Quiz App v1</title>
</head>
<body>
    <h1>Quiz App — v1</h1>
    <h2>Add Quiz</h2>

    <form method="POST">
        <input name="question" placeholder="Question" required>
        <br><br>
        <input name="a" placeholder="Option A" required>
        <input name="b" placeholder="Option B" required>
        <br><br>
        <input name="c" placeholder="Option C" required>
        <input name="d" placeholder="Option D" required>
        <br><br>
        <select name="answer">
            <option value="A">Correct: A</option>
            <option value="B">Correct: B</option>
            <option value="C">Correct: C</option>
            <option value="D">Correct: D</option>
        </select>
        <button type="submit">Add Quiz</button>
    </form>

    {% if message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            message = "Quiz question created successfully!"
    return render_template_string(HTML, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)