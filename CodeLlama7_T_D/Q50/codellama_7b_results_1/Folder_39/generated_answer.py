
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Loop through each string in the list
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]
        # Check if the current string is at least three characters long
        if len(current_string) >= 3:
            # Create a copy of the current string that we can modify
            modified_string = current_string.lower()
            # Sort the letters in the modified string
            sorted_letters = "".join(sorted(modified_string))
            # Loop through each string in the list again
            for j in range(len(my_list)):
                # Get the current string
                other_string = my_list[j]
                # Check if the current string is not the same as the original string
                if i != j:
                    # Create a copy of the current string that we can modify
                    modified_other_string = other_string.lower()
                    # Sort the letters in the modified string
                    sorted_letters_other = "".join(sorted(modified_other_string))
                    # Check if the two strings are anagrams of each other
                    if sorted_letters == sorted_letters_other:
                        # Increment the counter for the number of anagrams found
                        num_anagrams += 1
                        # If we have found at least 54 pairs of anagrams, return true
                        if num_anagrams >= 54:
                            return True
    # If we have not found any anagrams, return false
    return False
