from flask import Flask, request, jsonify
from detector.cheat_detector import detect_cheat

app = Flask(__name__)

@app.route("/event", methods=["POST"])
def handle_event():
    data = request.json
    result = detect_cheat(data)

    if result["cheater"]:
        return jsonify({"status": "blocked", "reason": result["reason"]}), 403
    
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(debug=True)
