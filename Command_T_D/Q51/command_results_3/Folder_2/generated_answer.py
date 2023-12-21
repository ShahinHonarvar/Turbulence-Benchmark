import re
def if_contains_anagrams(s):
    return sum(
        1
        for w in s
        if re.match(r'[a-z]{3,}', w.lower())
        for ww in s
        if re.match(r'[a-z]{3,}', ww.lower())
        if set(w.lower()) == set(ww.lower())
    ) <= 81
