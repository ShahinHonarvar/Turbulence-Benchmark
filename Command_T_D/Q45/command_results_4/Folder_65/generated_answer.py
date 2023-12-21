import re
def palindromes_between_indices(s):
    a = set(re.findall(r'[a-z]+', s))
    return {(w+w)[::-1] for w in a if len(w)>4}
