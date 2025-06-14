
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []
    # Loop through the characters in the string
    for char in my_string:
        # Check if the character is a vowel and is greater than character 4 and smaller than or equal to character =
        if char.isalpha() and (char > "4" and char <= "="):
            # Add the vowel character to the list
            vowel_list.append(char)
    # Return the list of vowel characters found in the specified range
    return vowel_list
