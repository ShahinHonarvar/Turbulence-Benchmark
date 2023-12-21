
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Skip strings that are too short
        if len(string1) < minimum_length:
            continue

        # Convert both strings to lowercase
        string1_lower = string1.lower()

        # Iterate over the remaining strings in the list
        for string2 in my_list[my_list.index(string1) + 1:]:
            # Skip strings that are too short
            if len(string2) < minimum_length:
                continue

            # Convert both strings to lowercase
            string2_lower = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(string1_lower) == sorted(string2_lower):
                # Increment the number of anagram pairs found
                anagram_pairs += 1

    # Return whether there are at most 29 pairs of anagrams in the given list
    return anagram_pairs <= 29
