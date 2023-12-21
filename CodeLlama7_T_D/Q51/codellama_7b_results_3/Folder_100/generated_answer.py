
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs
    num_pairs = 0
    # Iterate through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]
        # Check if the current string is an anagram of any other string in the list
        for j in range(i + 1, len(my_list))):
            # Get the second string to check
            sec_str = my_list[j]
            # Check if the two strings are anagrams of each other
            if sorted(curr_str) == sorted(sec_str):
                # Increment the number of anagram pairs
                num_pairs += 1
    # Return whether there are at most 98 pairs of anagrams in the given list
    return num_pairs <= 98
