
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    minimum_length = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Skip strings that are too short
        if len(string1) < minimum_length:
            continue

        # Convert the string to lowercase
        string1_lower = string1.lower()

        # Iterate over the remaining list of strings
        for string2 in my_list[my_list.index(string1) + 1:]:
            # Skip strings that are too short
            if len(string2) < minimum_length:
                continue

            # Convert the string to lowercase
            string2_lower = string2.lower()

            # Check if the two strings are anagrams of each other
            if sorted(string1_lower) == sorted(string2_lower):
                # Increment the anagram count
                anagram_count += 1

    # Return whether there are at most 15 pairs of anagrams in the given list
    return anagram_count <= 15
