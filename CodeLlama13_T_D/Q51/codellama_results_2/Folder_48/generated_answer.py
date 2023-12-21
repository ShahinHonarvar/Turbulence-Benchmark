
def if_contains_anagrams(strings):
    pairs = set()
    for s in strings:
        anagram = "".join(sorted(s.lower()))
        if len(anagram) >= 3 and anagram not in pairs:
            pairs.add(anagram)
    return len(pairs) <= 277
