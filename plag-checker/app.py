from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Перевірка на плагіат</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; background-color: #f0f0f0; }
        textarea { width: 100%; height: 150px; margin-bottom: 20px; padding: 10px; }
        input[type="submit"] { padding: 10px 20px; font-size: 16px; }
        .result { margin-top: 20px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>Онлайн перевірка на плагіат</h1>
    <form method="post">
        <label>Текст 1:</label><br>
        <textarea name="text1" required>{{ text1 }}</textarea><br>
        <label>Текст 2:</label><br>
        <textarea name="text2" required>{{ text2 }}</textarea><br>
        <input type="submit" value="Перевірити">
    </form>
    {% if result is not none %}
    <div class="result">
        Співпадіння: {{ result }}%
    </div>
    {% endif %}
</body>
</html>
"""

def calculate_similarity(text1, text2):
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    if not words1 or not words2:
        return 0
    common = words1.intersection(words2)
    similarity = len(common) / max(len(words1), len(words2)) * 100
    return round(similarity, 2)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text1 = ""
    text2 = ""
    if request.method == "POST":
        text1 = request.form["text1"]
        text2 = request.form["text2"]
        result = calculate_similarity(text1, text2)
    return render_template_string(HTML_TEMPLATE, result=result, text1=text1, text2=text2)

if __name__ == "__main__":
    app.run(debug=True)