
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    min_length = 3

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        s1 = my_list[i]

        # Check if the current string is at least three characters long
        if len(s1) >= min_length:
            # Convert the current string to lowercase
            s2 = s1.lower()

            # Iterate over the remaining strings in the list
            for j in range(i+1, len(my_list)):
                # Get the next string
                s3 = my_list[j]

                # Check if the next string is at least three characters long
                if len(s3) >= min_length:
                    # Convert the next string to lowercase
                    s4 = s3.lower()

                    # Check if the current string and the next string are anagrams of each other
                    if sorted(s2) == sorted(s4):
                        # Increment the number of pairs found
                        num_pairs += 1

                        # If the number of pairs found is greater than or equal to 38, return false immediately
                        if num_pairs >= 38:
                            return False

    # If no more pairs can be found, return true
    return True
