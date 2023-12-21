
def if_contains_anagrams(my_list):
    # Initialize variables
    num_pairs = 0
    anagram_length = 3

    # Loop through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_string = my_list[i]

        # Loop through the remaining strings
        for j in range(i+1, len(my_list)):
            # Get the next string
            next_string = my_list[j]

            # Check if the current and next strings are anagrams
            if sorted(curr_string) == sorted(next_string):
                num_pairs += 1

                # If there are more than 474 pairs of anagrams, return False
                if num_pairs > 474:
                    return False

        # If the current string has at least three letters and is not a palindrome, return True
        if len(curr_string) >= anagram_length and curr_string != curr_string[::-1]:
            return True

    # If there are no pairs of anagrams, return False
    return False
