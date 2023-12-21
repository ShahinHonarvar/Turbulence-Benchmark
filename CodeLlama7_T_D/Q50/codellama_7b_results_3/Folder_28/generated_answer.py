
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of pairs of anagrams
    pair_counter = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Loop through each string in the list again
        for j in range(len(my_list)):
            # If we are not looking at the same string, check if it is an anagram
            if i != j:
                # Check if the current string and the string we are looking at now share the same letters
                if sorted(current_string.lower()) == sorted(my_list[j].lower()):
                    # Increment the pair counter if they do
                    pair_counter += 1

    # Return true if there are at least 81 pairs of anagrams in the list, otherwise return false
    return pair_counter >= 81
