
def if_contains_anagrams(my_list):
    # Initialize variables
    num_anagrams = 0
    min_length = 3

    # Loop through each string in the list
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of itself
        if lowercase_string == string:
            continue

        # Check if the string is an anagram of another string
        for other_string in my_list:
            # Ignore the original string
            if other_string == string:
                continue

            # Convert the other string to lowercase
            lowercase_other_string = other_string.lower()

            # Check if the two strings are anagrams of each other
            if sorted(lowercase_string) == sorted(lowercase_other_string):
                num_anagrams += 1

    # Check if there are at most 28 pairs of anagrams in the list
    return num_anagrams <= 28
