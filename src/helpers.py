
import logging
from textwrap import dedent
from time import time
from markdown import markdown
from flask import render_template, g, url_for


def format_description(description):
    dedented = dedent(description)
    return markdown(dedented)


def render_solution(solution, title, input=None):
    description = format_description(solution.__doc__)
    if (input == None):
        input = solution.__defaults__[0]
    try:
        answer = str(solution(input))
        duration = '%.3f' % (time() - g.start_time)
        return render_template('solution.html', title=title, description=description,
                               answer=answer, duration=duration, input=input)
    except Exception as e:
        logging.exception(e)
        return render_template('error.html')


def get_problem(rule, func):
    endpoint = rule.endpoint
    problem = {}
    problem['name'] = func.__doc__ or 'Untitled'
    problem['number'] = endpoint.split('_')[1]
    if (len(rule.arguments) == 0):
        problem['url'] = url_for(endpoint)
    else:
        problem['url'] = url_for(endpoint, input=7)
    return problem


def problems_list(url_map, globals):
    problems = []
    for rule in url_map.iter_rules():
        endpoint = rule.endpoint
        if ('problem_' not in endpoint):
            continue
        func = globals.get(endpoint)
        problem = get_problem(rule, func)
        problems.append(problem)
    return problems
