import re
def palindromes_between_indices(s):
    res = set(re.findall(r'(?=((?=([a-z]+?){6}))\1)', s[1:-1]))
    return res
