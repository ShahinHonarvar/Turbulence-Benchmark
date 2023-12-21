 def return_vowels(string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through each character in the string
    for char in string:
        # Check if the current character is a vowel
        if char in "aeiou":
            # Add the current character to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
