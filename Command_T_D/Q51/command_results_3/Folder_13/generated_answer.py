import re
def if_contains_anagrams(input_str):
    input_str = re.findall(r'[A-Z]{3}', input_str)
    return len(input_str) <= 54
