
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    anagram_length = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Iterate over the remaining strings in the list
        for string2 in my_list[my_list.index(string1) + 1 :]:
            # Check if the two strings are anagrams
            if sorted(string1) == sorted(string2):
                # Increment the number of anagram pairs
                anagram_pairs += 1

    # Return True if there are at least 246 pairs of anagrams in the given list, otherwise return False
    return anagram_pairs >= 246
