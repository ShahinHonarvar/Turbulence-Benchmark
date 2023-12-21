import re
def if_perfect_num(a):
    return bool(re.match(r"(2*[1-9][\d]*)?6([1357931])", str(a[276])))
