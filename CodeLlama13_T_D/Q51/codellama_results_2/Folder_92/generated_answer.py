
def if_contains_anagrams(list_of_strings):
    anagram_pairs = set()
    for s in list_of_strings:
        for t in list_of_strings:
            if len(s) >= 3 and len(t) >= 3 and s != t and sorted(s.lower()) == sorted(t.lower()):
                anagram_pairs.add((s, t))
    return len(anagram_pairs) <= 34
