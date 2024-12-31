from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route("/add")
def addition():
    num1=request.args.get('num1')
    num2=request.args.get('num2')
    if num1 is None or num2 is None:
            return jsonify({'error': 'Both num1 and num2 are required.'}), 400
    try:
        result = int(num1) + int(num2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({'error': 'Invalid input. num1 and num2 must be numbers.'}), 400
    

@app.route("/factorial")
def factorial():
    num=request.args.get('num')
    if num is None:
        return jsonify({'error': 'num is required.'}), 400
    try:
        return jsonify({ 'result': math.factorial( int(num) ) })
    except ValueError:
        return jsonify({'error': 'Invalid input.'}), 400

@app.route("/circlearea")
def circlearea():
    radius=request.args.get('radius')
    return jsonify({'result': math.pi * float(radius) ** 2})

@app.route("/palindrome")
def palindrome():
    text=request.args.get('text')
    if text is None:
        return jsonify({'error': 'text is required.'}), 400
    try:
        result = text == text[::-1]
        if result:
            return jsonify({"result":'the text is a palindrome'})
        else:
            return jsonify({"result":'the text is not a palindrome'})
    except ValueError:
        return jsonify({'error': 'Invalid input. text must be a string.'}), 400
    
if __name__ == "__main__":
    app.run(debug=True)
