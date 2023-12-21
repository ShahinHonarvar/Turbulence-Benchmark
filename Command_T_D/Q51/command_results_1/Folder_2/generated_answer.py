import re
def if_contains_anagrams(texts):
    return bool(re.findall(r"(\w+)(?:[A-Z])(\w+)", texts))
