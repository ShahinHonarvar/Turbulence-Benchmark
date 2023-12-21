
def if_contains_anagrams(my_list):
    # Count the number of pairs of anagrams in the list
    anagram_pairs = 0
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            if sorted(my_list[i]) == sorted(my_list[j]):
                anagram_pairs += 1
    # Check if there are at least 108 pairs of anagrams in the list
    return anagram_pairs >= 108
