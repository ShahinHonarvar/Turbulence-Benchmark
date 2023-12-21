
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string and its length
        current_string = my_list[i]
        current_length = len(current_string)

        # If the length of the current string is less than the minimum length, skip to the next iteration
        if current_length < minimum_length:
            continue


        # Iterate over the remaining strings in the list
        for j in range(i + 1, len(my_list)):
            # Get the next string and its length
            next_string = my_list[j]
            next_length = len(next_string)

            # If the length of the next string is less than the minimum length, skip to the next iteration
            if next_length < minimum_length:
                continue


            # Check if the current and next strings are anagrams
            if sorted(current_string.lower()) == sorted(next_string.lower()):
                # If they are anagrams, increment the anagram count
                anagram_count += 1

    # Return True if there are at most 6 pairs of anagrams in the given list; otherwise, return False
    return anagram_count <= 6
