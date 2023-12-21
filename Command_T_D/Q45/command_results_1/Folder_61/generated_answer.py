import re
def palindromes_between_indices(s):
    return set(re.findall(r'([a-z]{2,6})([a-z]{2,6})([a-z]{2,6})([a-z]{2,6})([a-z]{2,6})([a-z]{2,6})([a-z]{2,6})', s[0:7]))
