
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    min_len = 3

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        s1 = my_list[i]

        # Check if the length of the current string is greater than or equal to the minimum length
        if len(s1) >= min_len:
            # Convert the current string to lowercase
            s2 = s1.lower()

            # Iterate over the remaining strings in the list
            for j in range(i+1, len(my_list)):
                # Get the next string
                s3 = my_list[j]

                # Check if the length of the next string is greater than or equal to the minimum length
                if len(s3) >= min_len:
                    # Convert the next string to lowercase
                    s4 = s3.lower()

                    # Check if the current string and the next string are anagrams of each other
                    if sorted(s2) == sorted(s4):
                        # Increment the number of pairs found
                        num_pairs += 1

                        # If the number of pairs found is greater than or equal to 73, return True
                        if num_pairs >= 73:
                            return True
    # Return False if no anagrams were found
    return False
