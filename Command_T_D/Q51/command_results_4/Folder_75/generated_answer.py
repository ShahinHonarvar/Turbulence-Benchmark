import re
def if_contains_anagrams(s):
    if re.search(r"(\w+[A-Z])\1", s):
        if len(s) > 10 and len(s) <= 55:
            return True
    return False
