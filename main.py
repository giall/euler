from flask import Flask, render_template, g
from time import time

from solutions import summation_of_primes, pandigital_prime

app = Flask(__name__)


def render_solution(solution, input=None):
    title = solution.__doc__
    if (input == None):
        input = solution.__defaults__[0]
    answer = solution(input)
    duration = time() - g.start_time
    return render_template('solution.html', title=title, answer=answer, duration='%.3f' % duration)


@app.before_request
def before_request():
    g.start_time = time()


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/10')
def ten():
    return render_solution(summation_of_primes)


@app.route('/41')
def forty_one():
    return render_solution(pandigital_prime, 10000)


if __name__ == '__main__':
    app.run(debug=True)
