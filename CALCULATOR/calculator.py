from flask import Flask, render_template, request
from math import *

app = Flask(__name__)

# ===== FUNCTIONS =====
def add(a, b): return a + b
def dif(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return "Error" if b == 0 else a / b
def mod(a, b): return a % b
def sin_val(a): return sin(radians(a))
def cos_val(a): return cos(radians(a))
def tan_val(a): return tan(radians(a))
def cot_val(a):
    t = tan(radians(a))
    return "Undefined" if t == 0 else 1 / t
def sec_val(a):
    c = cos(radians(a))
    return "Undefined" if c == 0 else 1 / c
def cosec_val(a):
    s = sin(radians(a))
    return "Undefined" if s == 0 else 1 / s
def sqrt_val(a): return sqrt(a)
def pow_val(a, b): return pow(a, b)
def sqr(a): return a ** 2

# ===== FLASK ROUTE =====
@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    num1 = request.form.get("num1", "")
    num2 = request.form.get("num2", "")

    if request.method == "POST":
        try:
            op = request.form["op"]

            # BACKSPACE
            if op == "back":
                if num2:
                    num2 = num2[:-1]
                elif num1:
                    num1 = num1[:-1]
                return render_template("index.html", result=result, num1=num1, num2=num2)

            # CLEAR
            if op == "C":
                return render_template("index.html", result="", num1="", num2="")

            # DECIMAL POINT
            if op == ".":
                if num2:
                    if "." not in num2:
                        num2 += "."
                else:
                    if "." not in num1:
                        num1 += "."
                return render_template("index.html", result=result, num1=num1, num2=num2)

            # Convert to float
            a = float(num1) if num1 else 0
            b = float(num2) if num2 else 0

            # OPERATIONS
            if op == "+":
                result = add(a, b)
            elif op == "-":
                result = dif(a, b)
            elif op == "*":
                result = mul(a, b)
            elif op == "/":
                result = div(a, b)
            elif op == "%":
                result = mod(a, b)
            elif op == "sin":
                result = sin_val(a)
            elif op == "cos":
                result = cos_val(a)
            elif op == "tan":
                result = tan_val(a)
            elif op == "cot":
                result = cot_val(a)
            elif op == "sec":
                result = sec_val(a)
            elif op == "cosec":
                result = cosec_val(a)
            elif op == "sqrt":
                result = sqrt_val(a)
            elif op == "sqr":
                result = sqr(a)
            elif op == "pow":
                result = pow_val(a, b)

        except:
            result = "Error"

    return render_template("index.html", result=result, num1=num1, num2=num2)


if __name__ == "__main__":
    app.run(debug=True)
