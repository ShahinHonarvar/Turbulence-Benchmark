import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'\A([a-z]{3}){2}\Z', texts, flags=re.IGNORECASE))
