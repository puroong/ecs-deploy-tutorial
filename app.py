from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Main Page"

@app.route("/new")
def new():
    return "new"

@app.route("/health-check")
def health_check():
    return "ok"

@app.route("/new2")
def new_2():
    return "new2"

@app.route("/new3")
def new_3():
    return "new3"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
