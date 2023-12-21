
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagram pairs found
    pair_counter = 0

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string and its length
        curr_string = my_list[i]
        curr_length = len(curr_string)

        # Check if the current string is at least three characters long
        if curr_length >= 3:
            # Convert the current string to lowercase for case-insensitive comparison
            lowercase_string = curr_string.lower()

            # Iterate over the remaining strings in the list
            for j in range(i + 1, len(my_list)):
                # Get the next string and its length
                next_string = my_list[j]
                next_length = len(next_string)

                # Check if the next string is at least three characters long
                if next_length >= 3:
                    # Convert the next string to lowercase for case-insensitive comparison
                    lowercase_next_string = next_string.lower()

                    # Check if the current and next strings are anagrams
                    if sorted(lowercase_string) == sorted(lowercase_next_string):
                        # Increment the pair counter if the strings are anagrams
                        pair_counter += 1

    # Return true if there are at least 155 pairs of anagrams in the given list; otherwise, return false
    return pair_counter >= 155
