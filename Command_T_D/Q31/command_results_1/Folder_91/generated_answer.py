import re
def if_perfect_num(a):
    return bool(re.search(r'(2\d{7}|3\d{5}|5\d{3}|6\d{2})', str(a[6])))
