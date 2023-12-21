import re
def palindromes_between_indices(s):
    return set(re.findall(r"<(?P<s>.{5,})>(?P=s)>", s))
