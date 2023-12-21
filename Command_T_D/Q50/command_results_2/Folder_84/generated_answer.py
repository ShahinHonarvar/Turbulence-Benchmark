import re
def if_contains_anagrams(text):
    return bool(re.findall(r"(\w+)(?:[A-Z])?(?:[a-z])?(?:[0-9])+", text))
