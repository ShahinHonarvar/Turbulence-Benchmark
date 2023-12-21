
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs and length
    anagram_pairs = 0
    minimum_length = 3

    # Iterate through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]
        # Check if the length is greater than or equal to the minimum length
        if len(current_string) >= minimum_length:
            # Convert the current string to lowercase for case-insensitive comparison
            lowercase_current_string = current_string.lower()

            # Iterate through the remaining strings in the list
            for j in range(i + 1, len(my_list)):
                # Get the next string in the list
                next_string = my_list[j]
                # Check if the length is greater than or equal to the minimum length
                if len(next_string) >= minimum_length:
                    # Convert the next string to lowercase for case-insensitive comparison
                    lowercase_next_string = next_string.lower()

                    # Check if the current string and next string are anagrams
                    if sorted(lowercase_current_string) == sorted(lowercase_next_string):
                        # Increment the number of anagram pairs
                        anagram_pairs += 1

            # Check if there are at most 475 pairs of anagrams in the given list
            if anagram_pairs <= 475:
                # Return true if there are at most 475 pairs of anagrams in the given list
                return True
            else:
                # Return false if there are more than 475 pairs of anagrams in the given list
                return False
        else:
            # If the length is less than the minimum length, return false
            return False
    else:
        # If no string meets the minimum length requirement, return false
        return False
