
def if_contains_anagrams(my_list):
    # Check that the list is not empty
    if len(my_list) == 0:
        return False

    # Create a set of unique strings in the list
    unique_strings = set()

    for string in my_list:

        # Convert the string to lowercase and sort it
        sorted_string = "".join(sorted(string.lower()))

        # Check if the sorted string is already in the set of unique strings
        if sorted_string in unique_strings:

            # If it is, return True
            return True

        else:

            # Add the sorted string to the set of unique strings
            unique_strings.add(sorted_string)

    # If we reach this point, there are no anagrams in the list
    return False
