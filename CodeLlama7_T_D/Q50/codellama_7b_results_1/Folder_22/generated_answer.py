
def if_contains_anagrams(my_list):
    # Define the length of at least three for anagram detection
    min_length = 3

    # Initialize a counter for the number of pairs of anagrams found
    num_pairs = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        str1 = my_list[i]

        # Loop through each remaining string in the list
        for j in range(i+1, len(my_list))):
            # Get the second string
            str2 = my_list[j]

            # Check if the two strings are anagrams of each other
            if sorted(str1) == sorted(str2):
                # Increment the counter for number of pairs found
                num_pairs += 1

    # Return True if there are at least 72 pairs of anagrams in the given list; otherwise, return False.
    return num_pairs >= 72
