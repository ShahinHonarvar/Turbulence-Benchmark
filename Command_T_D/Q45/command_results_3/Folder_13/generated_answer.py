import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?=([^aieou]))(.*?)([aieou].*?)\1', s))
