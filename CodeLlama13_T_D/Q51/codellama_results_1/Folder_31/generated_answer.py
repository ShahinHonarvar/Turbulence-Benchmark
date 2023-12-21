
def if_contains_anagrams(my_list):
    anagram_pairs = []
    for s1 in my_list:
        for s2 in my_list:
            if s1 != s2 and len(s1) >= 3 and len(s2) >= 3 and sorted(s1.lower()) == sorted(s2.lower()):
                anagram_pairs.append((s1, s2))
    return len(anagram_pairs) <= 65
