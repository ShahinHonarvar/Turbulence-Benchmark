import re
def if_contains_anagrams(a):
    return len(re.findall(r"<(.*?)>", re.findall(r"<(.*?)>", a))) > 15
