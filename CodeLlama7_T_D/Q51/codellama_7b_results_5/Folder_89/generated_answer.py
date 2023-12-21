
def if_contains_anagrams(my_list):
    # Initialize counter for pairs of anagrams
    pair_counter = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is a palindrome
        if current_string == current_string[::-1]:
            # If it is, then remove it from the list
            del my_list[i]
            # Decrement the loop counter by 1
            i -= 1

        # Loop through each remaining string in the list
        for j in range(len(my_list) - 1):
            # Get the current and next strings
            current_string = my_list[j]
            next_string = my_list[j + 1]

            # Check if the current string is an anagram of the next string
            if sorted(current_string) == sorted(next_string):
                # If it is, then increment the pair counter by 1
                pair_counter += 1

    # Return True if there are at most 73 pairs of anagrams in the given list; otherwise, return False
    if pair_counter <= 73:
        return True
    else:
        return False
