
def if_contains_anagrams(my_list):
    # count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(my_list) - 1)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_pairs += 1
    # check if there are at least 189 pairs of anagrams in the list
    return anagram_pairs >= 189
