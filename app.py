
from flask import Flask, request, render_template_string

app = Flask(__name__)

QUESTIONS = [
    {
        "question": "Which language is used for web page styling?",
        "options": ["Python", "CSS", "SQL", "Java"],
        "answer": "CSS"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "Central Processing Unit",
            "Computer Personal Unit",
            "Central Program Utility",
            "Control Processing User"
        ],
        "answer": "Central Processing Unit"
    },
    {
        "question": "Which data structure follows FIFO?",
        "options": ["Stack", "Tree", "Queue", "Graph"],
        "answer": "Queue"
    }
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Quiz App v2</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 700px;
            margin: 40px auto;
            padding: 20px;
            background: #f3f4f6;
        }
        h1 { color: #1d4ed8; }
        .question {
            background: white;
            padding: 18px;
            margin: 16px 0;
            border-radius: 10px;
        }
        button {
            background: #2563eb;
            color: white;
            padding: 12px 20px;
            border: 0;
            border-radius: 6px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Quiz App — Version 2</h1>
    <p>Attempt all three questions and submit your answers.</p>
    <form method="POST">
        {% for q in questions %}
        <div class="question">
            <h3>{{ loop.index }}. {{ q.question }}</h3>
            {% for option in q.options %}
            <label>
                <input type="radio" name="q{{ loop.index0 }}"
                       value="{{ option }}" required>
                {{ option }}
            </label><br>
            {% endfor %}
        </div>
        {% endfor %}
        <button type="submit">Submit Quiz</button>
    </form>
    {% if score is not none %}
        <h2>Your score: {{ score }}/{{ questions|length }}</h2>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def quiz():
    score = None

    if request.method == "POST":
        score = sum(
            request.form.get(f"q{i}") == q["answer"]
            for i, q in enumerate(QUESTIONS)
        )

    return render_template_string(
        HTML, questions=QUESTIONS, score=score
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
