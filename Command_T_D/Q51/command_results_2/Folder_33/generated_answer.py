import re
def if_contains_anagrams(s):
    anagrams = set()
    for el in s:
        if len(el) >= 3 and re.match(r'[A-Z]+', el.lower()):
            for an in range(len(el)):
                for b in range(an+1, len(el)):
                    c = el[:an] + el[b:]
                    if c not in anagrams:
                        anagrams.add(c)
                    elif c in anagrams:
                        anagrams.remove(c)
    return len(anagrams) <= 85
