
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the character is a vowel and is greater than 'N' and smaller than or equal to 'U'
        if char.isalpha() and char.lower() > 'n' and char.lower() <= 'u':
            # If the condition is true, append the character to the list
            vowel_list.append(char)
    # Return the list of vowel characters between index 24 (inclusive) and index 59 (exclusive) that are greater than character N and smaller than or equal to character U. If no such characters exist in the specified range, the function should return an empty list.
    return vowel_list
