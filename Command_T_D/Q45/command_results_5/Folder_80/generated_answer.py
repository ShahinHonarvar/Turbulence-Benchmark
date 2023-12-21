import re
def palindromes_between_indices(s):
    letters = re.findall("[A-Z]+", s[3:-8])
    return {l[::-1] for l in [ letters + l + letters for l in letters ] if l}
