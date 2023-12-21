
def if_contains_anagrams(my_list):
    # Set of all anagram pairs in the list
    pair_set = set()
    for word1 in my_list:
        for word2 in my_list:
            if len(word1) < 3 or len(word2) < 3:
                continue

            if sorted(word1.lower()) == sorted(word2.lower()):
                pair_set.add((word1, word2))
    return len(pair_set) <= 392
