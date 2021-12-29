from flask import Flask, jsonify, request

# Initialize app 
app = Flask(__name__)

# Define what the app does 
@app.get("/greet")
def index():
    name = request.args.get("name")
    if not name:
        return jsonify({"status":"Please provide a name"})

    response = {"date" : f"Hello, {name} !"}
    return jsonify(response)
