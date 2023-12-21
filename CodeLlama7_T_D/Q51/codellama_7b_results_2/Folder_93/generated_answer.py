
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    case_insensitive_comparison = False

    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of the English letters
        if sorted(lowercase_string) == sorted('abcdefghijklmnopqrstuvwxyz'):
            # Increment the anagram count
            anagram_count += 1

            # Check if the string meets the length requirement
            if len(string) >= 3:
                # Set the case-insensitive comparison flag to True
                case_insensitive_comparison = True

    # Return False if there are more than 36 pairs of anagrams in the given list
    if anagram_count > 36:
        return False

    # Return True if there are at most 36 pairs of anagrams in the given list, and the case-insensitive comparison flag is set to True
    else:
        return case_insensitive_comparison
