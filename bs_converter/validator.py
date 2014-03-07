__author__ = 'archmagece'

import re


def is_number(num_str):
    try:
        int(num_str)
        float(num_str)
        return True
    except ValueError:
        return False
    pass


def is_int(num_str):
    try:
        int(num_str)
        return True
    except ValueError:
        return False
    pass


def is_float(num_str):
    try:
        float(num_str)
        return True
    except ValueError:
        return False
    pass


def is_compatible(regex_str, compare_str):
    p = re.compile(regex_str)
    m = p.match(compare_str)
    if m is None:
        return False
    else:
        return True
    #m.group()
    pass


def is_exists(regex_str, compare_str):
    p = re.compile(regex_str)
    m = p.search(compare_str)
    if m is None:
        return False
    else:
        return True
    #m.group()
    pass

