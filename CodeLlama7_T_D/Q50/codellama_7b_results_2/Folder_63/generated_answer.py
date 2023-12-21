
def if_contains_anagrams(string_list):
    # Initialize a counter for the number of anagrams found
    num_anagrams = 0

    # Iterate over each string in the list
    for string1 in string_list:

        # Ignore strings that are less than three characters long
        if len(string1) < 3:
            continue


        # Convert both strings to lowercase before comparing them
        string1 = string1.lower()

        # Iterate over each string in the list again
        for string2 in string_list:

            # Ignore strings that are less than three characters long
            if len(string2) < 3:
                continue


            # Convert both strings to lowercase before comparing them
            string2 = string2.lower()

            # If the two strings are anagrams, increment the counter
            if sorted(string1) == sorted(string2):
                num_anagrams += 1

    # Return True if there are at least 89 pairs of anagrams in the list; otherwise return False
    return num_anagrams >= 89
