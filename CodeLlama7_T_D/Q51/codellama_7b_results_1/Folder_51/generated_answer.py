
def if_contains_anagrams(my_list):
    # Initialize counter for number of anagram pairs
    num_anagram_pairs = 0

    # Iterate over each string in the list
    for i in range(len(my_list)):
        # Get current string
        curr_string = my_list[i]

        # Check if current string is an anagram of another string in the list
        for j in range(len(my_list)):
            # Skip checking against itself
            if i == j:
                continue

            # Get other string
            other_string = my_list[j]

            # Check if current string and other string are anagrams of each other
            if sorted(curr_string) == sorted(other_string):
                num_anagram_pairs += 1

    # Return True if there are at most 116 pairs of anagrams in the given list, otherwise return False
    return num_anagram_pairs <= 116
