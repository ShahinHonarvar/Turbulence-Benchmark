
def if_contains_anagrams(string_list):
    # Initialize variables
    num_pairs = 0
    min_length = 3

    # Iterate over the list of strings
    for string1 in string_list:
        # Ignore strings that are too short
        if len(string1) < min_length:
            continue

        # Iterate over the remaining strings
        for string2 in string_list[string_list.index(string1) + 1 : ]:
            # Check if the two strings are anagrams
            if sorted(string1) == sorted(string2):
                # Increment the number of pairs found
                num_pairs += 1

    # Return whether there are at least 77 pairs of anagrams in the given list
    return num_pairs >= 77
