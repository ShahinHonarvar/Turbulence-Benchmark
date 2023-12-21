import re
def if_contains_anagrams(s):
    return len(set(s)) <= 88 and all(x.lower() != y.lower() for x, y in zip(s, s)) and len(s) > 2 and all(
        re.match(r'(?=([a-z]))\1+$', x.lower()) for x in s
    )
