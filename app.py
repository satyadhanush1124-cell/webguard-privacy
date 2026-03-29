from flask import Flask, render_template, jsonify
from collections import defaultdict
import random
import psutil

app = Flask(__name__)
risk_scores = defaultdict(int)

def get_risk_level(score):
    if score < 20:
        return "LOW"
    elif score < 60:
        return "MEDIUM"
    else:
        return "HIGH"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data")
def data():
    apps = []
    for proc in psutil.process_iter(['name']):
        try:
            name = proc.info['name']
            # Simulate network connections count
            conns = random.randint(0, 10)
            risk_scores[name] += conns
            level = get_risk_level(risk_scores[name])
            apps.append({
                "app": name,
                "connections": conns,
                "score": risk_scores[name],
                "level": level,
                "reason": f"Simulated reason for {name}",
                "suggestion": f"Simulated suggestion for {name}"
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return jsonify(apps)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
