
def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for s1 in string_list:
        for s2 in string_list:
            if len(s1) >= 3 and len(s2) >= 3:
                if sorted(s1.lower()) == sorted(s2.lower()):
                    anagram_pairs += 1
    return anagram_pairs >= 72
