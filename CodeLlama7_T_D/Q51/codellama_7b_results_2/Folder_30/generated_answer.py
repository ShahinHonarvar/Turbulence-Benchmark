
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    length_threshold = 3

    # Iterate over the list and check for anagrams
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if the current string is an anagram of another string in the list
        for j in range(len(my_list)):
            # Skip the same string
            if i == j:
                continue

            # Get the other string
            other_string = my_list[j]

            # Check if the current string is an anagram of the other string
            if sorted(current_string.lower()) == sorted(other_string.lower()):
                # Increment the anagram count
                anagram_count += 1

                # If there are more than 28 pairs of anagrams, return False
                if anagram_count > 28:
                    return False

                # If the length of the current string is less than the length threshold, return False
                if len(current_string) < length_threshold:
                    return False

                # If the length of the other string is less than the length threshold, return False
                if len(other_string) < length_threshold:
                    return False

    # If there are no more than 28 pairs of anagrams in the list, return True
    return True
