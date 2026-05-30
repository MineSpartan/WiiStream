from flask import Flask, jsonify, send_file, request
import requests
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Twitch public API (no OAuth needed for basic data)
CLIENT_ID = "YOUR_TWITCH_CLIENT_ID"

def twitch_get(endpoint, params):
    headers = {"Client-ID": CLIENT_ID}
    r = requests.get("https://api.twitch.tv/helix/" + endpoint,
                     headers=headers, params=params)
    return r.json()

@app.route("/list_streams")
def list_streams():
    data = twitch_get("streams", {"first": 20})

    out = []
    for s in data.get("data", []):
        out.append({
            "name": s["user_login"],
            "title": s["title"],
            "game": s["game_name"],
            "viewers": s["viewer_count"],
            "thumbnail_url": s["thumbnail_url"]
                .replace("{width}", "320")
                .replace("{height}", "180")
        })

    return jsonify(out)

@app.route("/search/<query>")
def search(query):
    data = twitch_get("search/channels", {"query": query, "first": 20})

    out = []
    for s in data.get("data", []):
        if not s["is_live"]:
            continue

        out.append({
            "name": s["broadcaster_login"],
            "title": s["title"],
            "game": s["game_name"],
            "viewers": s["viewer_count"],
            "thumbnail_url": s["thumbnail_url"]
        })

    return jsonify(out)

@app.route("/thumb")
def thumb():
    url = request.args.get("url")
    if not url:
        return "Missing URL", 400

    r = requests.get(url)
    img = Image.open(BytesIO(r.content))
    img = img.resize((200, 112), Image.BILINEAR)

    buf = BytesIO()
    img.save(buf, format="JPEG")
    buf.seek(0)

    return send_file(buf, mimetype="image/jpeg")

@app.route("/stream/<channel>")
def stream(channel):
    # Wii will connect to your transcoder here
    return jsonify({
        "url": f"http://yourserver:8080/transcode/{channel}"
    })

@app.route("/categories")
def categories():
    return jsonify([
        "Just Chatting",
        "Games",
        "IRL",
        "Music",
        "Esports"
    ])

@app.route("/")
def home():
    return "WiiStream Backend Prototype Running"