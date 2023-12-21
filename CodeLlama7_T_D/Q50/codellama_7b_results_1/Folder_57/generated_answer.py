
def if_contains_anagrams(my_list):
    # Initialize variables
    count = 0
    anagram_count = 0

    # Loop through the list and check for anagrams
    for i in range(len(my_list)):
        # Get the current string
        curr_str = my_list[i]

        # Check if the current string is an anagram of any other string in the list
        for j in range(i+1, len(my_list))):
            # Get the other string
            other_str = my_list[j]

            # Check if the two strings are anagrams
            if sorted(curr_str.lower()) == sorted(other_str.lower()):
                count += 1

        # Check if there are at least 50 pairs of anagrams in the list
        if count >= 50:
            anagram_count += 1

    # Return true if there are at least 50 pairs of anagrams in the list; otherwise, return false.
    return anagram_count >= 1
