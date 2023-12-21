
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    length_threshold = 3

    # Iterate over the list of strings
    for string1 in my_list:
        # Convert both strings to lowercase
        string1_lower = string1.lower()

        # Iterate over the remaining strings
        for string2 in my_list[my_list.index(string1) + 1 :]:
            # Convert both strings to lowercase
            string2_lower = string2.lower()

            # If the two strings are not equal and they have at least one character in common, check if they are anagrams
            if string1_lower != string2_lower and len(set(string1_lower) & set(string2_lower))) {
                # If the two strings are anagrams, increment the anagram count
                anagram_count += 1

                # If the anagram count is greater than or equal to 73, return True
                if anagram_count >= 73:
                    return True

    # If no anagrams were found, return False
    return False
