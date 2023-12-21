
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_chars = False
    # Iterate through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]
        # Check if the current string is at least 3 characters long
        if len(curr_str) >= 3:
            three_or_more_chars = True
            # Create a copy of the current string without any spaces
            no_spaces = curr_str.replace(" ", "")
            # Iterate through the rest of the list of strings
            for j in range(i + 1, len(my_list)):
                # Get the next string
                next_str = my_list[j]
                # Check if the next string is at least 3 characters long and has no spaces
                if (len(next_str) >= 3) and (next_str.count(" ") == 0):
                    # Check if the two strings are anagrams of each other
                    if sorted(no_spaces) == sorted(next_str):
                        # Increment the anagram count
                        anagram_count += 1
                        # Break out of the inner loop since we've found another anagram
                        break
            # If we found at least one anagram, then we can break out of the outer loop
            if anagram_count >= 49:
                return True
    # If we made it to the end of the function without finding any anagrams, then return False
    return False
