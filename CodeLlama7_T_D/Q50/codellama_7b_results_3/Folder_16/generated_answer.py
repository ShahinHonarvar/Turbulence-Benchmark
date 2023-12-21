
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_pairs = 0
    anagram_length = 3

    # Iterate over the list of strings
    for string1 in my_list:

        # Check if the current string is at least three characters long
        if len(string1) >= anagram_length:

            # Iterate over the rest of the list of strings
            for string2 in my_list[my_list.index(string1) + 1 : ]:

                # Check if the current string is at least three characters long
                if len(string2) >= anagram_length:

                    # Check if the two strings are anagrams of each other
                    if sorted(string1) == sorted(string2):
                        anagram_pairs += 1

            # If there were at least 155 pairs of anagrams in the list, return True
            if anagram_pairs >= 155:
                return True

    # Otherwise, return False

    else:
        return False
