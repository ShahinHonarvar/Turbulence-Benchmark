
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs and their lengths
    num_anagram_pairs = 0
    min_anagram_length = 3

    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list)):
            # Check if the two strings are anagrams of each other
            if sorted(my_list[i]) == sorted(my_list[j]):
                # Increment the number of anagram pairs
                num_anagram_pairs += 1

    # Return True if there are at least 108 pairs of anagrams in the list, and False otherwise
    return num_anagram_pairs >= 108
