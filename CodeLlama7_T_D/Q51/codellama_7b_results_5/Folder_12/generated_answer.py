
def if_contains_anagrams(str_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Iterate over the list of strings
    for i in range(len(str_list)):
        # Get the current string
        curr_str = str_list[i]

        # Iterate over the rest of the list of strings
        for j in range(i + 1, len(str_list))):
            # Get the next string
            next_str = str_list[j]

            # Check if the current and next strings are anagrams of each other
            if sorted(curr_str) == sorted(next_str):
                # If they are, add them to the dictionary of anagram pairs
                anagram_pairs[(curr_str, next_str)] = (i, j)

    # Check if there are more than 92 pairs of anagrams in the list of strings
    return len(anagram_pairs) <= 92
