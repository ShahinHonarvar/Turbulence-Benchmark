import re
def if_contains_anagrams(texts):
    if len(texts) < len(set(texts)):
        return True
    elif len(texts) == len(set(texts)):
        return False
    elif len(texts) > len(set(texts)):
        return False
    else:
        return sum(1 for s in texts if re.match(r'(?i)(?<=\A)(?P<s>.+)(?=\Z)', s)) >= 86
