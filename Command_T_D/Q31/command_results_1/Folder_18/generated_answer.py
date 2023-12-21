import re
def if_perfect_num(a):
    return bool(re.match(r"(\d+)(?=\D\1)", str(a[312])))
