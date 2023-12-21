
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    min_length = 3

    # Iterate over the list of strings
    for string in my_list:
        # Convert the current string to lowercase
        lowercase_string = string.lower()

        # Check if the current string is an anagram of itself
        if lowercase_string == string:
            continue

        # Check if the current string is an anagram of any other string in the list
        for other_string in my_list:
            # Convert the current string to lowercase
            lowercase_other_string = other_string.lower()

            # Check if the current string and the other string are anagrams
            if lowercase_string == lowercase_other_string:
                # Increment the number of anagram pairs found
                anagram_pairs += 1

    # Return true if there are at least 91 pairs of anagrams in the given list; otherwise, return false
    return anagram_pairs >= 91
