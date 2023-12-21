import re
def if_contains_anagrams(input_str):
    return bool(re.findall(r'(?i)(?<=.)(?!\1)[a-z]+\1', input_str, flags=re.I))
