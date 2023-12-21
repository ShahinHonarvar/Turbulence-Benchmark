
def if_contains_anagrams(my_list):
    # Get the number of elements in the list
    num_elements = len(my_list)
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0
    # Loop through each string in the list
    for i in range(num_elements):
        # Get the current string
        curr_string = my_list[i]
        # Convert the current string to lowercase
        lowercase_string = curr_string.lower()
        # Loop through each character in the current string
        for j in range(len(curr_string)):
            # Get the current character
            curr_char = lowercase_string[j]
            # If the current character is not a letter, skip to the next character
            if not curr_char.isalpha():
                continue

            # Loop through each string in the list starting at the index after the current string
            for k in range(i + 1, num_elements):
                # Get the current comparison string
                compare_string = my_list[k]
                # Convert the current comparison string to lowercase
                lowercase_compare_string = compare_string.lower()
                # Loop through each character in the current comparison string
                for l in range(len(compare_string)):
                    # Get the current character in the current comparison string
                    curr_char_compare = lowercase_compare_string[l]
                    # If the current character is not a letter, skip to the next character
                    if not curr_char_compare.isalpha():
                        continue

                    # If the current character and the current comparison string are anagrams of each other
                    if sorted(curr_char) == sorted(curr_char_compare):
                        # Increment the number of anagrams found
                        num_anagrams += 1

            # If there are at least 55 pairs of anagrams in the list
            if num_anagrams >= 55:
                # Return true
                return True

    # If there are no anagrams found in the list
    else:
        # Return false
        return False
