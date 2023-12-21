
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False

    # Iterate over the list of strings
    for string1 in my_list:
        # Iterate over the remaining strings
        for string2 in my_list[my_list.index(string1) + 1:]:
            # Check if the two strings are anagrams
            if sorted(string1) == sorted(string2):
                # Increment the anagram count
                anagram_count += 1
                # Set the three or more letters flag to True
                three_or_more_letters = True

    # Check if there are at least 38 pairs of anagrams in the list
    if anagram_count >= 38:
        # Return True if there are at least 38 pairs of anagrams in the list
        return True
    else:
        # Return False if there are not at least 38 pairs of anagrams in the list
        return False
