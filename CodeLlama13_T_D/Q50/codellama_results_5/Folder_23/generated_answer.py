
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s in strings:
        for t in strings[1:]:
            if len(s) >= 3 and len(t) >= 3 and len(s) == len(t) and sorted(s.lower()) == sorted(t.lower()):
                anagram_pairs += 1
    return anagram_pairs >= 67
