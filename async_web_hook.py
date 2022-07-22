from flask import Flask, request

app = Flask(__name__)

@app.post("/ok")
def handle_post():
    content_type = request.headers.get('Content-Type')
    if content_type == "application/json":
        json = request.json
        print(json)
        return json
    else:
        return 'Content-Type not supported'    

if __name__ == "__main__":
    app.run(debug=True)  
