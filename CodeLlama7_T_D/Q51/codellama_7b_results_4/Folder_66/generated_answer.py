
def if_contains_anagrams(my_list):
    # Initialize a counter for the number of anagram pairs
    pair_count = 0

    # Iterate over the list of strings
    for string1 in my_list:
        # Convert both strings to lowercase
        string1 = string1.lower()

        # Iterate over the remaining strings in the list
        for string2 in my_list[my_list.index(string1) + 1:]:
            # Convert the second string to lowercase
            string2 = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(string1) == sorted(string2):
                # Increment the counter for the number of anagram pairs
                pair_count += 1

    # Return True if there are at most 64 pairs of anagrams in the list, and False otherwise
    return pair_count <= 64
