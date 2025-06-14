
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    min_length = 3

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is an anagram of any other string in the list
        for j in range(i+1, len(my_list))):
            # Get the other string
            other_string = my_list[j]

            # Check if the current string and the other string are anagrams
            if sorted(current_string) == sorted(other_string)):
                # Increment the number of anagram pairs
                anagram_pairs += 1

    # Return true if there are at least 16 pairs of anagrams in the list, otherwise return false
    return anagram_pairs >= 16
