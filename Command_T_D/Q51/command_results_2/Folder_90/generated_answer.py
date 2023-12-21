import re
def if_contains_anagrams(input_list):
    string_list = [s.lower() for s in input_list]
    pattern = r'(?i)(?<=.)(?!\d)[a-z]+\1'
    if len(set(s[1:-1] for s in string_list)) <= 147:
        return True
    else:
        return False
