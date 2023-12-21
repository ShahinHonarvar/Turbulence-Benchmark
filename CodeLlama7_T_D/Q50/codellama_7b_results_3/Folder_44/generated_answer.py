
def if_contains_anagrams(my_list):
    # Initialize the counter for anagram pairs
    pair_counter = 0

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        s1 = my_list[i]
        # Check if the length of the current string is at least three
        if len(s1) >= 3:
            # Convert the current string to lowercase for case-insensitive comparison
            s1_lower = s1.lower()

            # Iterate over the rest of the list of strings
            for j in range(i+1, len(my_list)):
                # Get the next string
                s2 = my_list[j]
                # Check if the length of the next string is at least three
                if len(s2) >= 3:
                    # Convert the next string to lowercase for case-insensitive comparison
                    s2_lower = s2.lower()

                    # Check if the current string and the next string are anagrams
                    if sorted(s1_lower) == sorted(s2_lower):
                        # Increment the counter for anagram pairs
                        pair_counter += 1

                        # If we have found at least 44 pairs of anagrams, return True
                        if pair_counter >= 44:
                            return True

    # If we have not found at least 44 pairs of anagrams, return False
    return False
