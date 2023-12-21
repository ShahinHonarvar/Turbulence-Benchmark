def if_contains_anagrams(test_list):
    test_list = set(test_list)
    anagrams = set()
    for i in test_list:
        anagrams |= set(str(i).lower())
    return len(anagrams) <= 5
