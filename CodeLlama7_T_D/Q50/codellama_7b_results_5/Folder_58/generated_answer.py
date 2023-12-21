
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagram pairs
    pair_counter = 0

    # Iterate over the list of strings
    for string1 in my_list:
        # Convert both strings to lowercase for case-insensitive comparison
        string1_lowercase = string1.lower()

        # Iterate over the remaining strings in the list
        for string2 in my_list[my_list.index(string1) + 1:]:
            # Convert both strings to lowercase for case-insensitive comparison
            string2_lowercase = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(string1_lowercase) == sorted(string2_lowercase):
                # Increment the counter by 1
                pair_counter += 1

    # Return True if there are at least 411 pairs of anagrams in the given list; otherwise, return False
    return pair_counter >= 411
