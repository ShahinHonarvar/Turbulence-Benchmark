import re
def if_contains_anagrams(text):
    return bool(re.findall(r"<(.*?)>", text))
