
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        if len(s) < 3 or s.lower() in anagrams:
            continue
        anagrams.add(s.lower())
        for i in range(1, len(s)):
            substr = s[i:]
            if substr in anagrams:
                return True
    return False
