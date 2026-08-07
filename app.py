 # app.py
"""Small Flask status server — used as the web preview fallback (see main.py)."""
import os
 
from flask import Flask, jsonify
 
app = Flask(__name__)
 
STATUS_HTML = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Lyra Music — Preview</title>
<style>
  body { margin:0; min-height:100vh; display:flex; align-items:center; justify-content:center;
         background: radial-gradient(1200px 600px at 50% -10%, #1c2333 0%, #0b0e14 55%);
         font-family: system-ui, -apple-system, "Segoe UI", sans-serif; color:#e6e9f0; }
  .card { text-align:center; padding:2.5rem; }
  .dot { display:inline-block; width:10px; height:10px; border-radius:50%;
         background:#34d399; box-shadow:0 0 12px #34d399; margin-right:.5rem;
         animation:pulse 1.6s ease-in-out infinite; }
  @keyframes pulse { 50% { opacity:.45; } }
  h1 { font-size:2rem; margin:.5rem 0 .25rem; letter-spacing:.02em; }
  p  { color:#9aa4b8; margin:.35rem 0; }
  .muted { color:#5f6b80; font-size:.85rem; }
  code { background:#161b26; border:1px solid #242b3a; padding:.15rem .45rem;
         border-radius:6px; font-size:
…
