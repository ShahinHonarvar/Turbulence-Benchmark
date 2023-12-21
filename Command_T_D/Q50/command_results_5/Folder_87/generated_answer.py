import re
def if_contains_anagrams(list_of_strings):
    if len(list_of_strings) < 88:
        return False
    list_of_strings = list(filter(lambda s: len(s) >= 3, list_of_strings))
    return bool(re.findall(r'(?i)(?=.*\1)', list_of_strings))
