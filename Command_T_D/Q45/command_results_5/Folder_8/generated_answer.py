import re
def palindromes_between_indices(s):
    str_list = re.findall(r'[a-z]+', s.lower())
    if not str_list:
        return set()
    str_set = set(str_list)
    return set(str_set + str_set)
