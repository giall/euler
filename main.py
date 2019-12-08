from flask import Flask, render_template, g, url_for
from time import time
from sys import argv
import logging

from solutions import *

app = Flask(__name__)


def render_solution(solution, title, input=None):
    description = solution.__doc__
    if (input == None):
        input = solution.__defaults__[0]
    try:
        answer = str(solution(input))
        duration = '%.3f' % (time() - g.start_time)
        return render_template('solution.html', title=title, description=description, answer=answer, duration=duration)
    except Exception as e:
        logging.exception(e)
        return render_template('error.html')


def problems_list(url_map):
    problems = []
    for rule in url_map.iter_rules():
        if ('problem_' not in rule.endpoint):
            continue
        problem = {}
        func = globals().get(rule.endpoint)
        problem['name'] = func.__doc__
        problem['number'] = rule.endpoint.split('_')[1]
        if (len(rule.arguments) == 0):
            problem['endpoint'] = url_for(rule.endpoint)
        else:
            problem['endpoint'] = url_for(rule.endpoint, input=4)
        problems.append(problem)
    return problems


@app.before_request
def before_request():
    g.start_time = time()


@app.route('/')
def home():
    problems = problems_list(app.url_map)
    return render_template('index.html', problems=problems, len=len(problems))


@app.route('/problem/10')
def problem_10():
    """Summation of primes"""
    return render_solution(summation_of_primes, problem_10.__doc__)


@app.route('/problem/16')
def problem_16():
    """Power digit sum"""
    return render_solution(power_digit_sum, problem_16.__doc__)


@app.route('/problem/41/input/<int:input>')
def problem_41(input):
    """Pandigital prime"""
    return render_solution(pandigital_prime, problem_41.__doc__, input)


if __name__ == '__main__':
    debug = False
    for arg in argv[1:]:
        if (arg == '--debug'):
            debug = True
    app.run(debug=debug)
