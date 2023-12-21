
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize a counter for anagram pairs
    pair_counter = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]

        # Check if the current string is at least three characters long
        if len(curr_str) < 3:
            continue

        # Convert the current string to lowercase
        lower_case_str = curr_str.lower()

        # Loop through each subsequent string in the list
        for j in range(i + 1, len(my_list)):
            # Get the next string
            next_str = my_list[j]

            # Check if the next string is at least three characters long
            if len(next_str) < 3:
                continue

            # Convert the next string to lowercase
            lower_case_next_str = next_str.lower()

            # Check if the current and next strings are anagrams of each other
            if sorted(lower_case_str) == sorted(lower_case_next_str):
                # Increment the pair counter
                pair_counter += 1

    # Return whether there are at most 475 pairs of anagrams in the given list
    return pair_counter <= 475
