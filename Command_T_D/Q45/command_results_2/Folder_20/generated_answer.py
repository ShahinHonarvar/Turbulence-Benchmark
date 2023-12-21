import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?=([a-z]+\d){4}([a-z]+\d){3}([a-z]+\d){2}([a-z]+\d){1})', s))
