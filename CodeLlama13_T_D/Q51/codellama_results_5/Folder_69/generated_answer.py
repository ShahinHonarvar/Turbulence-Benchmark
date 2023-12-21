
def if_contains_anagrams(string_list):
    anagram_pairs = 0
    for s1 in string_list:
        for s2 in string_list:
            if s1 != s2 and len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                anagram_pairs += 1
    return anagram_pairs <= 58
