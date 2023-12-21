
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize a counter for the number of anagram pairs
    anagram_pairs = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Loop through each subsequent string in the list
        for j in range(i + 1, len(my_list)):
            # Get the next string
            next_string = my_list[j]

            # Check if the current and next strings are anagrams of each other
            if sorted(current_string.lower()) == sorted(next_string.lower()):
                # Increment the counter for anagram pairs
                anagram_pairs += 1

    # Check if there are more than 22 pairs of anagrams in the list
    return anagram_pairs <= 22
