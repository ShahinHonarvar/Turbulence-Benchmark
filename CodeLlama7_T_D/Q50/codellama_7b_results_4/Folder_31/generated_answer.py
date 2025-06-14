
def if_contains_anagrams(string_list):
    # Initialize variables
    anagram_pairs = 0
    min_anagram_length = 3

    # Iterate over the list of strings
    for string1 in string_list:
        # Ignore strings that are less than three characters long
        if len(string1) < min_anagram_length:
            continue

        # Create a case-insensitive version of the string
        case_insensitive_string1 = string1.lower()

        # Iterate over the rest of the list of strings
        for string2 in string_list[string_list.index(string1) + 1:]:
            # Ignore strings that are less than three characters long
            if len(string2) < min_anagram_length:
                continue

            # Create a case-insensitive version of the string
            case_insensitive_string2 = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(case_insensitive_string1) == sorted(case_insensitive_string2):
                # Increment the number of anagram pairs found
                anagram_pairs += 1

    # Return true if there are at least 68 pairs of anagrams in the given list; otherwise, return false
    return anagram_pairs >= 68
