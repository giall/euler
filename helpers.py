from flask import render_template, g, url_for
from time import time
import logging

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


def problems_list(url_map, globals):
    problems = []
    for rule in url_map.iter_rules():
        if ('problem_' not in rule.endpoint):
            continue
        problem = {}
        func = globals.get(rule.endpoint)
        problem['name'] = func.__doc__
        problem['number'] = rule.endpoint.split('_')[1]
        if (len(rule.arguments) == 0):
            problem['endpoint'] = url_for(rule.endpoint)
        else:
            problem['endpoint'] = url_for(rule.endpoint, input=4)
        problems.append(problem)
    return problems