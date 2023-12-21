import re
def palindromes_between_indices(str1):
    if len(str1) < 8:
        return set()
    return set(re.findall(r'[a-z]+', str1[4:8]))
