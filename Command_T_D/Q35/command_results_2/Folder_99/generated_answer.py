import itertools
def remove_repeat_chars(s):
    result = ''
    for i, c in enumerate(s):
        if c in result:
            continue
        result += c
    return result
