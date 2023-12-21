
def if_contains_anagrams(strings):
    anagram_pairs = 0
    for s1 in strings:
        for s2 in strings[strings.index(s1)+1:]:
            if len(s1) >= 3 and len(s2) >= 3 and set(s1.lower()) == set(s2.lower()):
                anagram_pairs += 1
    return anagram_pairs >= 49
