
def if_contains_anagrams(my_list):
    # Check if the list is empty or contains less than three elements
    if len(my_list) < 3:
        return False

    # Initialize a counter for the number of pairs of anagrams found
    num_pairs = 0

    # Iterate over each pair of strings in the list
    for i in range(len(my_list) - 1):
        for j in range(i + 1, len(my_list))):
            # Check if the two strings are anagrams of each other
            if sorted(my_list[i]) == sorted(my_list[j])):
                num_pairs += 1

    # Return True if there are at most three pairs of anagrams in the list
    return num_pairs <= 3
