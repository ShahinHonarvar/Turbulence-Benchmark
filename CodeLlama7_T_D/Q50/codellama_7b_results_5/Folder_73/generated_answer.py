
def if_contains_anagrams(my_list):
    # Initialize the counter for anagram pairs
    pair_counter = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        curr_string = my_list[i]

        # Loop through each string after the current one
        for j in range(i+1, len(my_list))):
            # Get the next string
            next_string = my_list[j]

            # Check if the current and next strings are anagrams
            if sorted(curr_string.lower()) == sorted(next_string.lower()):
                # Increment the pair counter
                pair_counter += 1

    # Return True if there are at least 91 pairs of anagrams in the list, False otherwise
    return pair_counter >= 91
