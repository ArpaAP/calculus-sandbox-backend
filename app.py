from flask import Flask, jsonify, request
from sympy import Symbol, SympifyError, integrate, sympify, latex
from sympy.core.mul import Mul
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/integrate", methods=['POST'])
def get_definite_integral():
    data: dict = request.get_json()

    print(data)

    try:
        parsed = sympify(data['expr'])
    except:
        return jsonify({'message': 'error'})

    x = Symbol('x')

    a = data.get('a', None)
    b = data.get('b', None)

    if isinstance(a, int) and isinstance(b, int):
        try:
            result = integrate(parsed, (x, a, b))
        except:
            return jsonify({'message': 'error'})

        return jsonify({
            'result_str': str(result),
            'latex': latex(result)
        })
    else:
        try:
            result = integrate(parsed, (x,))
        except:
            return jsonify({'message': 'error'})

        return jsonify({
            'latex': latex(result).replace(' ', '')
        }) 
