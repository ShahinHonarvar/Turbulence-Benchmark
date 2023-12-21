import re
def if_contains_anagrams(input_str):
    return bool(re.findall(r'(?i)(?=([a-z]+[a-z][a-z]))([a-z]+[a-z][a-z])', input_str))
