import re
def palindromes_of_specific_lengths(str):
    str = str.lower()
    m = re.search(r'[a-z]{13,49}(?=\W{17})[a-z]{13,49}', str)
    if m:
        return set(m.group().split())
    else:
        return set()
