
def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the character is a vowel and if it is greater than M and smaller than or equal to W
        if char.isalpha() and (char > 'M' and char <= 'W'):
            # Add the vowel to the list
            vowels.append(char)
    # Return the list of vowels
    return vowels
