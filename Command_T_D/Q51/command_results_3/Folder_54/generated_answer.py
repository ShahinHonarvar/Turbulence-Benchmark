import re
def if_contains_anagrams(texts):
    return not any(re.findall(r'(?i)(?=([A-Z]+[A-Z])))', str(a) for a in texts if a)
