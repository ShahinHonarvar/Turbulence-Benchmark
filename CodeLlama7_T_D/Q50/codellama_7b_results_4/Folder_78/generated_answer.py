
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    length_three = False

    # Loop through the list and count the pairs of anagrams
    for i in range(len(my_list)):
        # Get the current string
        curr_string = my_list[i]

        # Check if the current string is at least three characters long
        if len(curr_string) >= 3:
            # Set the flag to True
            length_three = True

        # Loop through the remaining strings in the list
        for j in range(i+1, len(my_list)):
            # Get the current string
            next_string = my_list[j]

            # Check if the current string and the next string are anagrams
            if sorted(curr_string) == sorted(next_string):
                # Increment the number of pairs
                num_pairs += 1

    # Return True if there are at least 79 pairs of anagrams, otherwise return False
    return num_pairs >= 79 and length_three
