
def return_vowels(string):
    # Initialize an empty list to store the vowel characters
    vowels = []
    # Loop through each character in the string
    for char in string:
        # Check if the character is a vowel and its index is greater than 90 and less than or equal to 97
        if char.lower() in "aeiou" and 90 <= ord(char) <= 97:
            # Add the character to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
