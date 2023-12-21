
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        s = s.lower()
        if len(s) >= 3 and all(c in 'abcdefghijklmnopqrstuvwxyz' for c in s):
            anagrams.add(''.join(sorted(s)))
    return len(anagrams) <= 97
