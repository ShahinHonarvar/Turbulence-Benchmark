import re
def if_contains_anagrams(texts):
    result = len(re.findall(r'(?i)(?=([a-z]+[0-9]+[a-z]+))(a-z)+[0-9]+[a-z]+)', ' '.join(texts))) <= 116
    return bool(result)
