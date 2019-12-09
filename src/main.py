from time import time
from sys import argv
from flask import Flask, render_template, g, url_for
from helpers import problems_list, render_solution
import solutions

app = Flask(__name__)


def main():
    debug = False
    for arg in argv[1:]:
        if (arg == '--debug'):
            debug = True
    app.run(host='0.0.0.0', debug=debug)


@app.before_request
def before_request():
    g.start_time = time()


@app.route('/')
def home():
    problems = problems_list(app.url_map, globals())
    return render_template('index.html', problems=problems, len=len(problems))


@app.route('/problem/10')
def problem_10():
    """Summation of primes"""
    return render_solution(solutions.summation_of_primes, problem_10.__doc__)


@app.route('/problem/16')
def problem_16():
    """Power digit sum"""
    return render_solution(solutions.power_digit_sum, problem_16.__doc__)


@app.route('/problem/20')
def problem_20():
    """Factorial digit sum"""
    return render_solution(solutions.factorial_digit_sum, problem_20.__doc__)


@app.route('/problem/41/input/<int:input>')
def problem_41(input):
    """Pandigital prime"""
    return render_solution(solutions.pandigital_prime, problem_41.__doc__, input)


if __name__ == '__main__':
    main()
