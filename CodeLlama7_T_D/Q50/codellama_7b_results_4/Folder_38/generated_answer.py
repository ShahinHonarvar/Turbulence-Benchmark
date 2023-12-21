
def if_contains_anagrams(my_list):
    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Loop through each string in the list
    for string1 in my_list:

        # Check if the string is at least 3 characters long
        if len(string1) >= 3:

            # Convert the string to lowercase
            string1_lower = string1.lower()

            # Loop through each string in the list again
            for string2 in my_list:

                # Check if the current string is not the same as the first string
                if string2 != string1:

                    # Convert the second string to lowercase
                    string2_lower = string2.lower()

                    # Check if the two strings are anagrams of each other
                    if sorted(string1_lower) == sorted(string2_lower):

                        # Add the pair to the dictionary of anagram pairs
                        anagram_pairs[(string1, string2)] = True

    # Check if there are at least 24 pairs of anagrams in the list
    return len(anagram_pairs) >= 24
