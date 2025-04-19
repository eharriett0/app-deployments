from flask import Flask, request, redirect, render_template, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST, Histogram

import redis
import os

app = Flask(__name__, template_folder="templates")
redis_host = os.getenv("REDIS_HOST", "localhost")
r = redis.Redis(host=redis_host, port=6379, decode_responses=True)

REQUESTS = Counter("http_requests_total", "Total HTTP Requests")
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency")
ERRORS = Counter("http_request_errors_total", "Total Errors")
MESSAGES_WRITTEN = Counter("guestbook_messages_total", "Messages written to Redis")

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.before_request
def before_request():
    REQUESTS.inc()

@app.route("/", methods=["GET", "POST"])
@REQUEST_LATENCY.time()
def index():
    if request.method == "POST":
        message = request.form.get("message")
        if message:
            r.lpush("guestbook", message)
            MESSAGES_WRITTEN.inc()
        return redirect("/")

    messages = r.lrange("guestbook", 0, -1)
    print("📦 Rendering with messages:", messages)
    return render_template("index.html", messages=messages)

if __name__ == "__main__":
    print("🎯 Triggering CI build...")
    app.run(host="0.0.0.0", port=5000)