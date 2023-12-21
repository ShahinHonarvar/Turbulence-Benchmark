
def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Iterate through the characters in the string
    for char in my_string:
        # Check if the current character is a vowel
        if char in "aeiou":
            # Add the vowel to the list
            vowels.append(char)
    # Return the list of vowels
    return vowels
