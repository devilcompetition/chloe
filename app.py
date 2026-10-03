import os

from flask import Flask, jsonify, render_template, request

from sam_chatbot import SamBot

app = Flask(__name__)
bot = SamBot()
PORT = int(os.environ.get("PORT", "5000"))


@app.route("/")
def index():
    return render_template("chat.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()
    mode = (data.get("mode") or bot.mode).lower().strip()

    if not message:
        return jsonify({"reply": "Tell me something sweet, and I’ll listen."})

    if mode in {"romantic", "cyber", "pentest", "ctf", "all"}:
        bot.set_mode(mode)

    reply = bot.get_reply(message, mode=mode)
    return jsonify({"reply": reply, "mode": bot.mode})


@app.route("/reminders/due")
def due_reminders():
    return jsonify({"reminders": bot.get_due_reminders()})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
