
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    minimum_length = 3

    # Iterate through the list and find pairs of anagrams
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            if sorted(my_list[i]) == sorted(my_list[j])):
                anagram_pairs += 1

    # Return true if there are at least 123 pairs of anagrams in the given list
    return anagram_pairs >= 123
