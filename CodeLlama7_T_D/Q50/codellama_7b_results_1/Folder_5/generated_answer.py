
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagram pairs and strings
    num_pairs = 0
    for i in range(len(my_list)):
        # Get the current string and its length
        current_string = my_list[i]
        current_length = len(current_string)
        # If the current string is not at least three characters long, skip it
        if current_length < 3:
            continue

        # Iterate over the remaining strings in the list
        for j in range(i + 1, len(my_list)):
            # Get the next string and its length
            next_string = my_list[j]
            next_length = len(next_string)
            # If the next string is not at least three characters long, skip it
            if next_length < 3:
                continue

            # If the current and next strings are anagrams of each other, increment the number of anagram pairs
            if sorted(current_string.lower()) == sorted(next_string.lower()):
                num_pairs += 1
                break

    # Return true if there are at least 21 pairs of anagrams in the given list; otherwise, return false
    return num_pairs >= 21
