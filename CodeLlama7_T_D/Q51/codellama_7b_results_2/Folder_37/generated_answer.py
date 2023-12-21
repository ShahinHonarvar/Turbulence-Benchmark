
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    min_length = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Get the length of the first string
        len1 = len(string1)

        # Check if the length of the first string is at least three
        if len1 >= min_length:
            # Iterate over the remaining strings
            for string2 in my_list[my_list.index(string1) + 1:]:
                # Get the length of the second string
                len2 = len(string2)

                # Check if the length of the second string is at least three
                if len2 >= min_length:
                    # Check if the strings are anagrams
                    if sorted(string1) == sorted(string2):
                        # Increment the number of anagram pairs
                        anagram_pairs += 1

                    # Check if there are more than 206 anagram pairs
                    if anagram_pairs > 206:
                        # Return false
                        return False

    # Return true if there are at most 206 anagram pairs, otherwise return false
    return anagram_pairs <= 206
