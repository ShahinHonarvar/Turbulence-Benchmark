
def if_contains_anagrams(my_list):
    anagram_pairs = 0
    for s1 in my_list:
        for s2 in my_list:
            if len(s1) >= 3 and len(s2) >= 3 and set(s1.lower()) == set(s2.lower()):
                anagram_pairs += 1
    return anagram_pairs <= 401
