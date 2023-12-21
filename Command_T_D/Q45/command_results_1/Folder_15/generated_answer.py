import re
def palindromes_between_indices(s):
    r = set(re.findall(r'(?i)(?P<p>[a-z]){2}(?P<q>[a-z]){2}(?P=p)', s))
    return r
