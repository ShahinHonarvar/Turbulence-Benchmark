
def if_contains_anagrams(strings):
    anagrams = set()
    for s in strings:
        if len(s) < 3 or any(c not in 'abcdefghijklmnopqrstuvwxyz' for c in s.lower()):
            continue
        key = tuple(sorted(s.lower()))
        if key in anagrams:
            return True
        anagrams.add(key)
    return False
