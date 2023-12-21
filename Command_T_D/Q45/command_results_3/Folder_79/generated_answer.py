import re
def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    else:
        return set(re.findall(r'((?i)(?<=.)[a-z]{3,})((?i)(?<=.)[a-z]{3,})', s))
