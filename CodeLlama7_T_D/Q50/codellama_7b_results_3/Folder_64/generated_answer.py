
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagram pairs
    pair_count = 0

    # Iterate over the list of strings
    for i in range(len(my_list) - 1):
        # Get the current string and its length
        curr_str = my_list[i]
        curr_len = len(curr_str)

        # Check if the current string is an anagram of at least three characters
        if curr_len >= 3:
            # Create a copy of the current string for comparison
            compare_str = curr_str

            # Iterate over the rest of the list of strings
            for j in range(i + 1, len(my_list)):
                # Get the next string to compare with the current string
                next_str = my_list[j]

                # Check if the next string is an anagram of the current string
                if sorted(next_str) == sorted(compare_str):
                    # Increment the counter for the number of anagram pairs
                    pair_count += 1

        # If there are at least five anagram pairs in the list, return true
        if pair_count >= 5:
            return True

    # Otherwise, return false
    return False
