
def if_contains_anagrams(str_list):
    # Initialize variables
    num_pairs = 0
    min_length = 3

    # Iterate over the list of strings
    for str1 in str_list:
        # Check if the length of the string is greater than or equal to the minimum length
        if len(str1) >= min_length:
            # Convert the string to lowercase
            str1 = str1.lower()

            # Iterate over the rest of the strings in the list
            for str2 in str_list[str_list.index(str1)+1:]:
                # Check if the length of the second string is greater than or equal to the minimum length
                if len(str2) >= min_length:
                    # Convert the second string to lowercase
                    str2 = str2.lower()

                    # If the two strings are anagrams, increment the number of pairs
                    if sorted(str1) == sorted(str2):
                        num_pairs += 1

                        # If there are at least 60 pairs of anagrams in the list, return True
                        if num_pairs >= 60:
                            return True

    # If there are not at least 60 pairs of anagrams in the list, return False
    return False
