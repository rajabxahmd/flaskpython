from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/add")
def addition():
    num1=request.args.get('num1')
    num2=request.args.get('num2')
    result = int(num1) + int(num2)
    return jsonify({"result": result})

if __name__ == "__main__":
    app.run(debug=True)
