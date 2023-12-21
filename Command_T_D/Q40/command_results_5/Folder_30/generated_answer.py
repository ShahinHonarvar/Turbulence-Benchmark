import re
def return_n_smallest_chars(s):
    s += '*'
    s += '#'
    s += '#'
    s += '*'
    s += '#'
    s += '#'
    s += '*'
    m = re.match(r'<#([^#]*?)#>', s)
    if m:
        return m.group(1)
    else:
        return s
