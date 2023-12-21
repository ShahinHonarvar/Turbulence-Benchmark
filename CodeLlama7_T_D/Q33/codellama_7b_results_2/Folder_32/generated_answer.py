
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowels = []
    # Iterate through the characters in the string
    for char in my_string:
        # Check if the character is a vowel and if it is greater than character b and smaller than or equal to character z
        if char.isalpha() and char > 'b' and char <= 'z':
            # If the condition is true, add the character to the list of vowels
            vowels.append(char)
    # Return the list of vowel characters between index 45 (inclusive) and index 76 (exclusive) that are greater than character b and smaller than or equal to character z
    return vowels
