
def if_contains_anagrams(string_list):
    # Initialize the number of pairs to 0
    num_pairs = 0
    # Loop through each string in the list
    for i in range(len(string_list)):
        # Get the current string
        string1 = string_list[i]
        # Loop through each other string in the list
        for j in range(len(string_list))[1:]:
            # Get the second string
            string2 = string_list[j]
            # Check if the two strings are anagrams
            if sorted(string1) == sorted(string2):
                # Increment the number of pairs
                num_pairs += 1
    # Return whether there are at least 11 pairs of anagrams in the list
    return num_pairs >= 11
