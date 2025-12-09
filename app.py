from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Działa! To jest aplikacja w kontenerze Docker na porcie 8000."

if __name__ == "__main__":
    # ważne: host 0.0.0.0 i port 8000 (taki potem mapujemy w docker run)
    app.run(host="0.0.0.0", port=8000)
