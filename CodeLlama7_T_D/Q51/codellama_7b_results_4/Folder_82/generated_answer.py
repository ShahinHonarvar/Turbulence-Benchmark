
def if_contains_anagrams(string_list):
    # Get the number of strings in the list
    num_strings = len(string_list)
    # Initialize a counter for the number of anagram pairs
    pair_count = 0
    # Loop through each string in the list
    for i in range(num_strings):
        # Get the current string
        curr_string = string_list[i]
        # Loop through each other string in the list
        for j in range(num_strings):
            # Get the other string
            other_string = string_list[j]
            # Check if the current string and other string are anagrams of each other
            if sorted(curr_string.lower()) == sorted(other_string.lower()):
                # Increment the pair counter
                pair_count += 1

    # Return True if there are at most 40 pairs of anagrams in the given list, otherwise return False
    return pair_count <= 40
