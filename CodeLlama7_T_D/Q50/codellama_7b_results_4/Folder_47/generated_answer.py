
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0

    # Iterate through the list of strings
    for i in range(len(my_list)):
        # Check if the current string is an anagram of any previous strings
        for j in range(i + 1, len(my_list))):
            # If the current string is an anagram of any previous string, increment the number of pairs found
            if sorted(my_list[i]) == sorted(my_list[j])):
                num_pairs += 1

    # Return whether there are at least 47 pairs of anagrams in the given list
    return num_pairs >= 47
