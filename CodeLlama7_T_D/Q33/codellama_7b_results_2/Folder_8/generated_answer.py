
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowels = []
    # Iterate through the characters in the string
    for char in my_string:
        # Check if the character is a vowel and its index is between 64 and 82 (inclusive) and smaller than or equal to 'z'
        if char.isalpha() and 64 <= ord(char) <= 82 and char <= 'z':
            # If the condition is true, add the character to the list of vowel characters
            vowels.append(char)
    # Return the list of vowel characters
    return vowels
