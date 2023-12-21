
def if_contains_anagrams(strings):
    # Initialize variables
    anagram_count = 0
    string_length = 3

    # Loop through each string in the list
    for string in strings:
        # Convert the string to lowercase
        string = string.lower()

        # Check if the string is at least three characters long
        if len(string) >= string_length:
            # Create a new list of all the anagrams of the string
            anagram_list = []

            # Loop through each character in the string
            for char in string:
                # Check if the character is already in the anagram list
                if char not in anagram_list:
                    # Add the character to the anagram list
                    anagram_list.append(char)

            # Check if there are at most 88 pairs of anagrams in the anagram list
            if len(anagram_list) <= 88:
                # Increment the anagram count
                anagram_count += 1

    # Return whether or not there were at most 88 pairs of anagrams in the given list
    return anagram_count <= 88
