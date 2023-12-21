import re
def palindromes_between_indices(str):
    str = re.sub(r'[^a-z0-9]+', '', str)
    return set(re.findall(r'(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])' + str, str))
