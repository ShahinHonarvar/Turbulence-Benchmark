
def if_contains_anagrams(string_list):
    anagram_pairs = []
    for s1 in string_list:
        for s2 in string_list:
            if len(s1) >= 3 and len(s2) >= 3 and set(s1.lower()) == set(s2.lower()):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) >= 246
