
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of the anagram pairs
    pair_count = 0
    min_length = 3

    # Loop through the list and check for anagrams
    for i in range(len(my_list)):
        # Get the current string and its length
        s1 = my_list[i]
        l1 = len(s1)

        # Check if the current string is long enough to be a candidate for an anagram
        if l1 >= min_length:
            # Loop through the rest of the list and check for anagrams
            for j in range(i+1, len(my_list)):
                # Get the next string and its length
                s2 = my_list[j]
                l2 = len(s2)

                # Check if the two strings are anagrams of each other
                if sorted(s1) == sorted(s2):
                    # Increment the pair count
                    pair_count += 1

    # Return True if there are at least 55 pairs of anagrams in the list, False otherwise
    return pair_count >= 55
