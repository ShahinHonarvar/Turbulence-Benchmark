
def if_contains_anagrams(my_list):
    # Initialize variables to keep track of anagrams
    anagram_count = 0
    pair_count = 0

    # Iterate over the list of strings
    for i in range(len(my_list)):
        # Get the current string
        current_string = my_list[i]

        # Check if there are any anagrams in the current string
        for j in range(i + 1, len(my_list)):
            # Get the other string to compare with the current string
            other_string = my_list[j]
            # Check if the two strings are anagrams
            if sorted(current_string) == sorted(other_string):
                # Increment the anagram count
                anagram_count += 1

                # If there are at least three pairs of anagrams, return True
                if anagram_count >= 3:
                    return True
