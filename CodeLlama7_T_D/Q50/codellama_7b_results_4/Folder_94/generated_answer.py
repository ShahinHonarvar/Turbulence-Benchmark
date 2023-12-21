
def if_contains_anagrams(my_list):
    # Initialize variables
    count = 0
    len3 = 0

    # Iterate over the list of strings
    for string in my_list:
        # Convert the current string to lowercase
        string_lower = string.lower()

        # Check if there are any other strings in the list that are anagrams of the current string
        for other_string in my_list:
            # If the current string and the other string are not the same, check if they are anagrams
            if string != other_string:
                # Convert the other string to lowercase
                other_string_lower = other_string.lower()
                # Check if the current string and the other string are anagrams
                if sorted(string_lower) == sorted(other_string_lower):
                    # Increment the count of anagram pairs found
                    count += 1

        # If there are at least three strings in the list that are not the same, check if they are all anagrams of each other
        if len3 >= 3:
            # Initialize a variable to keep track of whether or not all strings are anagrams of each other
            is_anagram = True

            # Iterate over the list of strings
            for string in my_list:
                # Convert the current string to lowercase
                string_lower = string.lower()

                # Check if the current string is not an anagram of all other strings
                if sorted(string_lower) != sorted(my_list[0].lower()):
                    # Set the variable to False
                    is_anagram = False

            # If all strings are anagrams of each other, return True
            if is_anagram:
                return True

    # If there are not at least four pairs of anagrams found in the list, return False
    if count < 46:
        return False
