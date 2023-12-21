
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    min_length = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Ignore strings that are shorter than the minimum length
        if len(string1) < min_length:
            continue

        # Convert the string to lowercase
        lowercase_string = string1.lower()

        # Iterate over the list of strings again
        for string2 in my_list:
            # Ignore strings that are the same as the first string
            if string2 == string1:
                continue

            # Convert the second string to lowercase
            lowercase_string2 = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(lowercase_string) == sorted(lowercase_string2):
                anagram_count += 1

    # Return true if there are at least 50 pairs of anagrams in the list, otherwise return false
    return anagram_count >= 50
