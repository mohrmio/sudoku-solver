from flask import Flask, render_template, request
from sudoku import solve
app = Flask(__name__)

@app.route('/')
def main_page():
    return render_template('entry.html',name=None)

@app.route('/solve',methods=['POST'])
def solve_request():
    # sanitize input and transform
    l = [int(v) if v.isdigit() else 0 for k,v in request.form.items()]
    input_grid = [l[i:i+9] for i in range(0,len(l),9)]
    return str(solve(input_grid))
