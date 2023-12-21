import re
def if_contains_anagrams(s):
    anagrams = {}
    for x in s:
        y = re.sub(r'[A-Z]', '', x).lower()
        if len(y) >= 3:
            if y not in anagrams:
                anagrams[y] = []
            anagrams[y].append(x)
    return len(anagrams) <= 14
