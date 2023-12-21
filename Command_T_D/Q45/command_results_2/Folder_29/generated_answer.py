import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?P<pal>(?:[a-z])))\1', s[2:-9:-1])
