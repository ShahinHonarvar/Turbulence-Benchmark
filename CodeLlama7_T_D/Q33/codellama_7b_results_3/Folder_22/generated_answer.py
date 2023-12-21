
def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the character is a vowel
        if char in "aeiou":
            # Add the character to the list of vowels
            vowels.append(char)
    return vowels
