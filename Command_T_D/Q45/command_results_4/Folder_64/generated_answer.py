import re
def palindromes_between_indices(s):
    # code by nishant403
    return {m.group() for m in re.finditer(r'[a-z]{4}(?=\w){4}[a-z]{4}', s[4:-5])}
