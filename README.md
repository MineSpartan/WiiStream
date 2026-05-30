# WiiStream

WiiStream is a homebrew Twitch client for the Nintendo Wii.  
It allows the Wii to browse Twitch streams, view categories, search channels, load thumbnails, and play live streams using a lightweight backend server.

This repository contains:
- The **Wii homebrew app** (in `/wii`)
- The **backend server** (in `/backend`) used to fetch Twitch data and resize thumbnails

---

## Features (Prototype Version)

- Browse live Twitch streams
- Search for channels
- View stream titles, games, and viewer counts
- Load thumbnails resized for the Wii
- Basic categories list
- Stream playback via external transcoder (coming soon)
- No OAuth required
- No chat yet (planned)

---

## Backend Setup

The backend is a simple Python Flask server that provides:
- `/list_streams` — list of live streams
- `/search/<query>` — search Twitch channels
- `/thumb?url=` — thumbnail resizing for Wii
- `/categories` — simple category list
- `/stream/<channel>` — stream URL placeholder

- ### Requirements

Install dependencies:

pip install -r backend/requirements.txt

Code

### Run the backend

python backend/backend.py

Code

The server will run on:

http://localhost:5000

Code

To use it on your Wii, replace `localhost` with your computer's LAN IP (e.g. `192.168.1.50`).

---

## Deploying the Backend Online

You can host the backend for free using:
- Railway
- Fly.io
- Render
- LocalTunnel
- Cloudflare Tunnel

Make sure the backend is accessible over **HTTP** (not HTTPS), since the Wii cannot use HTTPS.

---

## Wii App Setup

The Wii homebrew app (in `/wii`) connects to the backend using the IP or domain you configure in the settings menu.

Example:

Backend URL: http://your-backend-url-here

Code

---

## Roadmap

- Read-only chat (anonymous)
- Full chat with OAuth backend
- Emotes and badges
- Followed channels
- Stream transcoder for stable playback
- UI improvements and overlays

---

## Third Party Tools Used

- Uses Tinyh264 Decoder
- Uses Helix AAC Decoder

## License

MIT License
