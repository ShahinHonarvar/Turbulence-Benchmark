import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?<=\w)(?=\w)\1+\w+(?=\w)\1+', texts))
