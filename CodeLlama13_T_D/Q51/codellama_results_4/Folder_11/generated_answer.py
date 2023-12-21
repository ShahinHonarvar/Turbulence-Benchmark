
def if_contains_anagrams(strings):
    anagrams = set()
    for string in strings:
        s = ''.join(sorted(string.lower()))
        if len(s) >= 3 and s not in anagrams:
            anagrams.add(s)
            if len(anagrams) > 41:
                return False
    return True
