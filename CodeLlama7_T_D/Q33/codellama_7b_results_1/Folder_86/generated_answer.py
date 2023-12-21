
def return_vowels(string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through the characters in the string
    for char in string:
        # Check if the character is a vowel and its index is between 273 and 275 (inclusive)
        if char.lower() in "aeiou" and 273 <= string.index(char) <= 275:
            # Add the vowel to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
