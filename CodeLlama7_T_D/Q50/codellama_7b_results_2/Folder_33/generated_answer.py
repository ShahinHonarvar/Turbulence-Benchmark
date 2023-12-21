
def if_contains_anagrams(my_list):
    # Check if the length of the list is at least 140
    if len(my_list) < 140:
        return False

    # Create a dictionary to store the anagram pairs
    anagram_pairs = {}

    # Loop through each string in the list
    for string in my_list:

        # If the length of the string is at least three, continue
        if len(string) < 3:
            continue

        # Create a copy of the string with all lowercase letters
        lowercase_string = string.lower()

        # Sort the characters in the string to create an anagram
        sorted_anagram = "".join(sorted(lowercase_string))

        # If the sorted anagram is already in the dictionary, continue
        if sorted_anagram in anagram_pairs:
            continue

        # Create a list of the possible anagrams of the string
        possible_anagrams = []

        # Loop through each character in the string
        for char in lowercase_string:

            # If the character is not already in the list, add it to the list
            if char not in possible_anagrams:
                possible_anagrams.append(char)

        # Loop through each possible anagram of the string
        for anagram in possible_anagrams:

            # If the sorted anagram is already in the dictionary, continue
            if sorted_anagram in anagram_pairs:
                continue

            # Create a list of the possible anagrams of the string that are shorter than three characters
            short_anagrams = []

            # Loop through each character in the string
            for char in lowercase_string:

                # If the character is not already in the list, add it to the list
                if char not in short_anagrams:
                    short_anagrams.append(char)

            # Check if there are at least three characters in the string that are shorter than three characters
            if len(short_anagrams) < 3:
                continue

            # Add the sorted anagram to the dictionary with a value of the list of possible anagrams of the string
            anagram_pairs[sorted_anagram] = possible_anagrams

    # Check if there are at least 140 pairs of anagrams in the list
    return len(anagram_pairs) >= 140
