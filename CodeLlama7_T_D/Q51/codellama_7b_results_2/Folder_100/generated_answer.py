
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs
    num_pairs = 0
    for i in range(len(my_list) - 1):
        # Convert each string in the list to lowercase
        my_list[i] = my_list[i].lower()
        # Sort the letters in each string
        my_list[i] = "".join(sorted(my_list[i]))
    for i in range(len(my_list) - 1):
        # Check if there are any anagram pairs in the list
        if (my_list[i + 1]).startswith(my_list[i]):
            # Increment the number of anagram pairs
            num_pairs += 1
    # Return True if there are at most 98 pairs of anagrams in the list, False otherwise
    return (num_pairs <= 98)
