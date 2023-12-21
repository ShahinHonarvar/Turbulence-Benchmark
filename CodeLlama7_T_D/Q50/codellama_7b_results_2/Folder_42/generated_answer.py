
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of pairs of anagrams
    pair_counter = 0

    # Iterate over each string in the list
    for i in range(len(my_list)):
        # Get the current string and its length
        string1 = my_list[i]
        length1 = len(string1)

        # Check if the current string is an anagram of at least three characters
        if length1 >= 3:
            # Iterate over each subsequent string in the list
            for j in range(i + 1, len(my_list)):
                # Get the second string and its length
                string2 = my_list[j]
                length2 = len(string2)

                # Check if the current strings are anagrams of each other
                if sorted(string1) == sorted(string2):
                    # Increment the pair counter
                    pair_counter += 1

                    # Check if there are at least 233 pairs of anagrams in the list
                    if pair_counter >= 233:
                        # Return true if there are at least 233 pairs of anagrams in the list
                        return True

    # Return false if there are not at least 233 pairs of anagrams in the list
    return False
