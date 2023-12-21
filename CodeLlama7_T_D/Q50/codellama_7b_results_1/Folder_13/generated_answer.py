
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0

    # Iterate over the list of strings
    for string1 in my_list:

        # Compare each string with every other string
        for string2 in my_list:

            # If the two strings are not the same and have at least three characters, check if they are anagrams
            if string1 != string2 and len(string1) >= 3:

                # Check if the two strings are anagrams by converting them to lowercase and sorting them alphabetically
                sorted_lowercase_string1 = ''.join(sorted(string1.lower())))
                sorted_lowercase_string2 = ''.join(sorted(string2.lower())))

                # If the two strings are anagrams, increment the number of pairs by 1
                if sorted_lowercase_string1 == sorted_lowercase_string2:
                    num_pairs += 1

    # Return true if there are at least 144 pairs of anagrams in the given list, otherwise return false
    return num_pairs >= 144
