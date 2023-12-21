
def if_contains_anagrams(strings):
    # Get the length of at least three
    min_length = 3

    # Initialize a counter for the number of anagrams found
    num_anagrams = 0

    # Iterate over the strings in the list
    for string1 in strings:
        # Check if the current string is at least three characters long
        if len(string1) < min_length:
            continue

        # Convert the current string to lowercase
        string1_lower = string1.lower()

        # Iterate over the remaining strings in the list
        for string2 in strings[strings.index(string1)+1:]:
            # Check if the current string is at least three characters long
            if len(string2) < min_length:
                continue

            # Convert the current string to lowercase
            string2_lower = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(string1_lower) == sorted(string2_lower):
                # Increment the number of anagrams found
                num_anagrams += 1

    # Return whether there are at least 85 pairs of anagrams in the list
    return num_anagrams >= 85
