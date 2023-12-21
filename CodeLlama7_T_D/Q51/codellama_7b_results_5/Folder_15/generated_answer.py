
def if_contains_anagrams(my_list):
    # Check if the list is empty
    if len(my_list) == 0:
        return False

    # Initialize a counter for the number of anagrams
    num_anagrams = 0

    # Iterate over the list and compare each string to the others
    for i in range(len(my_list)):
        for j in range(i + 1, len(my_list))):
            # Check if the strings are anagrams of the English letters
            if sorted(my_list[i].lower()) == sorted(my_list[j].lower()):
                num_anagrams += 1

                # If there are more than 20 pairs of anagrams, return false
                if num_anagrams > 20:
                    return False

    # If no pairs of anagrams were found, return true
    return True
