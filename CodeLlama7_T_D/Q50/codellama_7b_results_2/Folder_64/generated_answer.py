
def if_contains_anagrams(my_list):
    # Check if the list is empty or None
    if my_list is None or len(my_list) == 0:
        return False

    # Initialize a counter for the number of pairs of anagrams found
    num_pairs = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        s1 = my_list[i]

        # Loop through each remaining string in the list
        for j in range(i + 1, len(my_list))):
            # Get the second string
            s2 = my_list[j]

            # Check if the two strings are anagrams of each other
            if sorted(s1) == sorted(s2):
                # Increment the counter for the number of pairs of anagrams found
                num_pairs += 1

                # If we have found at least 5 pairs of anagrams, return True
                if num_pairs >= 5:
                    return True
