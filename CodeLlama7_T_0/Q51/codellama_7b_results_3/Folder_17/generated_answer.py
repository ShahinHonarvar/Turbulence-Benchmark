
def if_contains_anagrams(my_list):
    # Initialize variables
    anagram_count = 0
    three_or_more_letters = False

    # Iterate over the list of strings
    for string in my_list:
        # Convert the string to lowercase
        lowercase_string = string.lower()

        # Check if the string is an anagram of the English letters
        if sorted(lowercase_string) == sorted('abcdefghijklmnopqrstuvwxyz'):
            # Increment the anagram count
            anagram_count += 1

            # Check if the string has at least three letters
            if len(lowercase_string) >= 3:
                # Set the flag to True
                three_or_more_letters = True

    # Return the result of the comparison
    return anagram_count <= 22 and three_or_more_letters
