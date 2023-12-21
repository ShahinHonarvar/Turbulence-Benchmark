import re
def palindromes_between_indices(s):
    m = re.fullmatch(r'(?P<a>[a-z])(?P<b>[a-z])(?P=a)(?P<c>[a-z])(?P=b)(?P<d>[a-z])(?P=c)(?P<e>[a-z])(?P=d)(?P<f>[a-z])(?P=e)(?P=f)', s)
    if m:
        return set(m.group(a).lower() for a in m.group(a))
    else:
        return set()
