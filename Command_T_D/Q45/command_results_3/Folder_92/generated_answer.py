import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]{4}((?<=a-z)a-z){2}([a-z]{2}(?<=z))', s))
