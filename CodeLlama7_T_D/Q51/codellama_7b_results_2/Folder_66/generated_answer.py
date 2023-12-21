
def if_contains_anagrams(my_list):
    # count the number of anagrams in the list
    anagram_count = 0
    for i in range(len(my_list) - 1)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j]):
                anagram_count += 1
    # return true if there are at most 64 pairs of anagrams in the list
    return anagram_count <= 64
