
def if_contains_anagrams(my_list):
    # Initialize variables
    count = 0
    anagram_pairs = []
    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]
        # Check if the current string is a palindrome
        if curr_str == curr_str[::-1]:
            # If it is, check if there are any other anagrams of the same length in the list
            for j in range(len(my_list)):
                # Get the other string
                other_str = my_list[j]
                # Check if the two strings are anagrams of each other
                if sorted(curr_str) == sorted(other_str):
                    # If they are, add them to the list of anagram pairs
                    anagram_pairs.append((i, j)))
            # Increment the count by the number of anagram pairs found
            count += len(anagram_pairs)
        # Reset the list of anagram pairs for the next iteration
        anagram_pairs = []
    # Return whether there are at least 136 pairs of anagrams in the given list
    return count >= 136
