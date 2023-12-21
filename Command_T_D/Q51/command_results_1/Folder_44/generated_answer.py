import re
def if_contains_anagrams(s):
    return sum(1 for x in s for y in s if re.fullmatch(x, y, flags=re.I)) <= 75
