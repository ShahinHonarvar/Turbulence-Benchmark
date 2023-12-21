import re
def if_contains_anagrams(texts):
    return len(re.findall(r"<(.*?)>", texts)) <= 67
