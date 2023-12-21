
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of another string in the list
        for other_string in my_list:
            # Skip the current string and the other string being compared
            if string == other_string:
                continue

            # Convert the other string to lowercase
            lowercase_other_string = other_string.lower()

            # Check if the two strings are anagrams of each other
            if sorted(lowercase_string) == sorted(lowercase_other_string):
                # Increment the anagram count
                anagram_count += 1

    # Return whether there are at most 86 pairs of anagrams in the list
    return anagram_count <= 86
