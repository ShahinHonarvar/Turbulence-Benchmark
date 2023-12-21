import re
def if_contains_anagrams(texts):
    return len(re.findall(r'(?i)(?<=.)(a)(b)(c)', texts)) <= 34
