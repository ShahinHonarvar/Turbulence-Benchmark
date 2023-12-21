
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string and its length
        s1 = my_list[i]
        l1 = len(s1)

        # If the length of the current string is at least 3, continue to the next step
        if l1 >= 3:
            # Loop through each subsequent string in the list
            for j in range(i+1, len(my_list)):
                # Get the second string and its length
                s2 = my_list[j]
                l2 = len(s2)

                # If the length of the second string is at least 3, continue to the next step
                if l2 >= 3:
                    # Check if the two strings are anagrams
                    if sorted(s1) == sorted(s2):
                        # Increment the number of pairs found
                        num_pairs += 1

                        # If the number of pairs found is at least 77, return True
                        if num_pairs >= 77:
                            return True
    # If no anagrams were found or the number of pairs found was less than 77, return False
    return False
