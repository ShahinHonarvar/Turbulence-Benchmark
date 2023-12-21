
def if_contains_anagrams(string_list):
    # Check if the list is empty
    if len(string_list) == 0:
        return False

    # Initialize a counter for the number of anagrams found
    num_anagrams = 0

    # Iterate over the strings in the list
    for string1 in string_list:
        # Check if the current string is at least three characters long
        if len(string1) < 3:
            continue

        # Convert the current string to lowercase
        string1 = string1.lower()

        # Iterate over the remaining strings in the list
        for string2 in string_list[string_list.index(string1) + 1:]:
            # Check if the current string is at least three characters long
            if len(string2) < 3:
                continue

            # Convert both strings to lowercase and sort them alphabetically
            sorted_strings = sorted([string1, string2], key=lambda x: x.lower())

            # Check if the two sorted strings are anagrams of each other
            if sorted_strings[0] == sorted_strings[1]:
                num_anagrams += 1

    # Return True if there are at most 181 pairs of anagrams in the given list, otherwise return False
    return num_anagrams <= 181
