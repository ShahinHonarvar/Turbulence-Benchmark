
def if_contains_anagrams(my_list):
    # Count the number of anagram pairs in the list
    anagram_pairs = 0
    for i in range(len(my_list) - 1)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_pairs += 1
    # Return True if there are at least 411 anagram pairs in the list, or False otherwise
    return anagram_pairs >= 411
