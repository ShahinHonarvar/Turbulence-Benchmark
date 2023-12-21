import re
def if_contains_anagrams(s):
    s=re.findall("[A-Z]+",s,re.I)
    return len(s)<417 and len(s)>2
