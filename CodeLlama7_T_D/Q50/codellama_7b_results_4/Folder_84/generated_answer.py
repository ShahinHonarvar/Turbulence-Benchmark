
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    anagram_length = 3

    # Iterate over the list of strings
    for string1 in my_list:

        # Iterate over the list of strings again, starting from the next element
        for string2 in my_list[my_list.index(string1) + 1 : ]:

            # Check if the two strings are anagrams
            if sorted(string1) == sorted(string2):

                # If they are, increment the anagram count and break out of the inner loop
                anagram_count += 1
                break

    # Return true if there are at least 108 pairs of anagrams in the given list
    return anagram_count >= 108
