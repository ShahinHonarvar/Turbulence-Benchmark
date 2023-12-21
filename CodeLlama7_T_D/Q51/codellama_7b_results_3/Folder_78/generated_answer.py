
def if_contains_anagrams(string_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string1 in string_list:
        # Check if the length of the current string is greater than or equal to the minimum length
        if len(string1) >= minimum_length:
            # Convert the current string to lowercase
            string1 = string1.lower()

            # Iterate over the list of strings again
            for string2 in string_list:
                # Check if the length of the current string is greater than or equal to the minimum length
                if len(string2) >= minimum_length:
                    # Convert the current string to lowercase
                    string2 = string2.lower()

                    # Check if the two strings are anagrams
                    if sorted(string1) == sorted(string2):
                        # Increment the anagram count
                        anagram_count += 1

                        # Check if there are at most 70 pairs of anagrams in the given list
                        if anagram_count <= 70:
                            return True

                        else:
                            return False

    return False
