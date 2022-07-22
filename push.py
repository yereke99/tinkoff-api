from flask import Flask, jsonify, request, json

app = Flask(__name__)

@app.route("/api/notification", methods=["POST"])
def notification():
    content_type = request.headers.get('Content-Type')
    if content_type == "application/json":
        json = request.json
        print(json)
        return json
    else:
        return 'Content-Type not supported'    


if __name__ == "__main__":
    app.run(debug=True)  