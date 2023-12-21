import re
def palindromes_between_indices(s):
    pat = re.compile(r'[a-z]{6}((?=.){6})[a-z]{6}')
    return {m[0] for m in pat.finditer(s[6:-8])}
