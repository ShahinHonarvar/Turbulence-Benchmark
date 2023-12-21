
def if_contains_anagrams(string_list):
    # Initialize variables for counting pairs of anagrams
    pair_count = 0

    # Iterate over the list of strings
    for string1 in string_list:
        # Convert both strings to lowercase
        string1 = string1.lower()

        # Iterate over the remaining strings in the list
        for string2 in string_list[string_list.index(string1) + 1:]:
            # Convert second string to lowercase
            string2 = string2.lower()

            # Check if both strings are anagrams of each other
            if sorted(string1) == sorted(string2):
                # Increment pair count by 1
                pair_count += 1

    # Return True if there are at most 416 pairs of anagrams in the list, otherwise return False
    return pair_count <= 416
