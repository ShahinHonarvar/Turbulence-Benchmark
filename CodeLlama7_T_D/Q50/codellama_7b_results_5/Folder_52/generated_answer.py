
def if_contains_anagrams(string_list):
    # Initialize variables
    anagram_pairs = 0
    min_length = 3

    # Iterate over the list of strings
    for i in range(len(string_list)):
        # Get the current string
        string1 = string_list[i]

        # Compare the current string with all other strings
        for j in range(len(string_list)):
            # Skip comparing the same string with itself
            if i == j:
                continue

            # Get the second string
            string2 = string_list[j]

            # Check if the strings are anagrams
            if sorted(string1) == sorted(string2):
                # Increment the number of anagram pairs
                anagram_pairs += 1

    # Return True if there are at least 58 pairs of anagrams, False otherwise
    return anagram_pairs >= 58
