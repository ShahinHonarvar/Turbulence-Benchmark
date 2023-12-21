
def return_vowels(my_string):
    # Define a list to store the vowel characters
    vowels = []
    # Loop through the characters in the string
    for char in my_string:
        # Check if the character is a vowel and
        # is greater than M and smaller than or equal to j
        if char.isalpha() and char > 'M' and char <= 'j':
            # Add the vowel character to the list
            vowels.append(char)
    # Return the list of vowel characters
    return vowels
