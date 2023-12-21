
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more = False

    # Loop through the list of strings
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is an anagram of another string in the list
        for j in range(i+1, len(my_list)):
            # Get the other string
            other_string = my_list[j]

            # Check if the current string and the other string are anagrams of each other
            if sorted(current_string) == sorted(other_string):
                # Increment the number of anagram pairs
                anagram_count += 1

                # If there are at least three strings in the list, set the variable to True
                if len(my_list) >= 3:
                    three_or_more = True

        # If there are at most four pairs of anagrams in the list, return True
        if anagram_count <= 4:
            return True

        # Otherwise, return False
        else:
            return False
