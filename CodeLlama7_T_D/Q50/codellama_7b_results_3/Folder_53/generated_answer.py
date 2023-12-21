
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize a counter for the number of anagrams found
    num_anagrams = 0

    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        curr_string = my_list[i]

        # Check if the current string is an anagram of any other strings in the list
        for j in range(len(my_list)):
            # Get the next string
            next_string = my_list[j]

            # Check if the current string and the next string are anagrams
            if curr_string != next_string:
                if sorted(curr_string.lower()) == sorted(next_string.lower()):
                    num_anagrams += 1

        # If the number of anagrams found is greater than or equal to 11, return True
        if num_anagrams >= 11:
            return True

    # Otherwise, return False
    return False
