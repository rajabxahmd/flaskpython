from flask import Flask, request, jsonify
import math

app = Flask(__name__)

@app.route("/add")
def addition():
    num1=request.args.get('num1')
    num2=request.args.get('num2')
    result = int(num1) + int(num2)
    return jsonify({"result": result})

@app.route("/factorial")
def factorial():
    num=request.args.get('num')
    return jsonify({ 'result': math.factorial( int(num) ) })

@app.route("/circlearea")
def circlearea():
    radius=request.args.get('radius')
    return jsonify({'result': math.pi * float(radius) ** 2})

@app.route("/palindrome")
def palindrome():
    text=request.args.get('text')
    result = text == text[::-1]
    if result:
        return jsonify({"result":'the text is a palindrome'})
    else:
        return jsonify({"result":'the text is not a palindrome'})
    
if __name__ == "__main__":
    app.run(debug=True)
