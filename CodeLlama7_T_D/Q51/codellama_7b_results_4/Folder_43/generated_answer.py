
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    anagram_length = 3

    # Iterate through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_string = my_list[i]
        # Check if there are at most 3 pairs of anagrams in the given list
        num_pairs += len([j for j in range(i + 1, len(my_list)) if sorted(curr_string.lower()) == sorted(my_list[j].lower())]) // 2)
        # If there are more than three pairs of anagrams, return False
        if num_pairs > anagram_length:
            return False

    # If there are at most three pairs of anagrams, return True
    return True
