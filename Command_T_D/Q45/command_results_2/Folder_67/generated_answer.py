import re
def palindromes_between_indices(str1):
    return set(re.findall(r'(?i)(?=.*?[a-z])[a-z]+(?=.*?[a-z])', str1[2:-2]))
