from flask import Flask, render_template, g, url_for
from time import time

from solutions import summation_of_primes, pandigital_prime

app = Flask(__name__)


def render_solution(solution, title, input=None):
    description = solution.__doc__
    if (input == None):
        input = solution.__defaults__[0]
    try:
        answer = solution(input)
        duration = time() - g.start_time
        return render_template('solution.html', title=title, description=description, answer=answer, duration='%.3f' % duration)
    except:
        return render_template('error.html')


def problems_list(url_map):
    problems = []
    for rule in url_map.iter_rules():
        if (rule.endpoint in ['home', 'static']):
            continue
        problem = {}
        problem['name'] = app.view_functions[rule.endpoint].__doc__
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
def ten():
    """Summation of primes"""
    title = ten.__doc__
    return render_solution(summation_of_primes, title)


@app.route('/problem/41/input/<int:input>')
def forty_one(input):
    """Pandigital prime"""
    title = forty_one.__doc__
    return render_solution(pandigital_prime, title, input)


if __name__ == '__main__':
    app.run()
