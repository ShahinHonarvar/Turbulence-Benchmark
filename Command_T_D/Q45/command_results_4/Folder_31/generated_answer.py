import re
def palindromes_between_indices(s):
    return set(re.findall(r'([a-z]{1,8})([a-z]{1,8})([a-z]{1,8})([a-z]{1,8})([a-z]{1,8})([a-z]{1,8})([a-z]{1,8})([a-z]{1,8})', s.lower()))
