from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

seed = 0

@app.route("/", methods=["POST", "GET"])
def handleMessage():
    global seed

    if request.method == "POST":
        subprocess.Popen(["python3", "stress_cpu.py"])
        return {"status": "Success"}, 200
    else:
        return socket.gethostname(), 200

if __name__ == '__main__':
    app.run(port=8080, host="0.0.0.0")