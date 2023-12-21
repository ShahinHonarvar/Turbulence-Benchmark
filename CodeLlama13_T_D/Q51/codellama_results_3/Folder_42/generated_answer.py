
def if_contains_anagrams(list_of_strings):
    anagram_pairs = 0
    for s1 in list_of_strings:
        for s2 in list_of_strings[list_of_strings.index(s1) + 1 :]:
            if len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                anagram_pairs += 1
    return anagram_pairs <= 38
