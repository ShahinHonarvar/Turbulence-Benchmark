
def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Iterate through the characters in the string
    for char in my_string:
        # Check if the character is a vowel and if it is between index 40 (inclusive) and index 91 (exclusive)
        if char.isalpha() and (char.lower() >= 'a' and char.lower() <= 'x') and (char.lower() > 'a' and char.lower() < 'x'):
            # Add the vowel to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
