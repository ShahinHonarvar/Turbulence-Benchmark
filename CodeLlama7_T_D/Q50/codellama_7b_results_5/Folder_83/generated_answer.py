
def if_contains_anagrams(my_list):
    # Get the length of the list
    my_len = len(my_list)
    # Initialize variables for counting pairs and anagrams
    pair_count = 0
    anagram_count = 0
    # Loop through the list
    for i in range(my_len):
        # Get the current string
        current_string = my_list[i]
        # Get the length of the current string
        current_length = len(current_string)
        # Check if the length is at least three
        if current_length >= 3:
            # Loop through the rest of the list
            for j in range(i + 1, my_len):
                # Get the next string
                next_string = my_list[j]
                # Check if the two strings are anagrams
                if sorted(current_string) == sorted(next_string):
                    # Increment the pair count
                    pair_count += 1
                    # Check if the pair count is at least 48
                    if pair_count >= 48:
                        # Return True
                        return True
            # If the pair count is less than 48, then increment the anagram count
            if pair_count < 48:
                anagram_count += 1
    # If the anagram count is greater than or equal to 3, then return False
    if anagram_count >= 3:
        return False
