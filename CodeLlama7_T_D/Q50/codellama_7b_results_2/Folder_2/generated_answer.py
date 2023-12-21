
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Ignore strings that are less than the minimum length
        if len(string1) < minimum_length:
            continue

        # Convert the first string to lowercase
        string1 = string1.lower()

        # Iterate over the remaining strings in the list
        for string2 in my_list[my_list.index(string1) + 1 :]:
            # Ignore strings that are less than the minimum length
            if len(string2) < minimum_length:
                continue

            # Convert the second string to lowercase
            string2 = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(string1) == sorted(string2):
                # Increment the anagram count
                anagram_count += 1

    # Return true if there are at least 246 pairs of anagrams in the list, otherwise return false
    return anagram_count >= 246
