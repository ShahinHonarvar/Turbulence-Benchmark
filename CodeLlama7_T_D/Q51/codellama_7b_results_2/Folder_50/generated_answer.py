
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    num_anagrams = 0
    # Iterate over the list of strings
    for string1 in my_list:
        # Iterate over the remaining strings
        for string2 in my_list[my_list.index(string1) + 1:]:
            # Check if the two strings are anagrams
            if sorted(string1) == sorted(string2):
                # Increment the number of pairs and anagrams
                num_pairs += 1
                num_anagrams += 1
    # Return True if there are at most 47 pairs of anagrams, False otherwise
    return num_pairs <= 47 and num_anagrams >= 3
