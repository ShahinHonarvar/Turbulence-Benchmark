
def if_contains_anagrams(strings):
    anagram_pairs = []
    for i, s1 in enumerate(strings):
        for j, s2 in enumerate(strings[i+1:]):
            if sorted(s1.lower()) == sorted(s2.lower()):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) >= 97
