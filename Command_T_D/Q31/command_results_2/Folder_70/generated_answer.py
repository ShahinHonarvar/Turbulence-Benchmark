import re
def if_perfect_num(a):
    return bool(re.search(r'(4*[1-9][^4]+6)', str(a[845])))
