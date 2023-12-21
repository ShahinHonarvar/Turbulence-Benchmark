
def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the current character is a vowel and it's index is greater than 31 and smaller than or equal to 37
        if char.lower() in "aeiou" and ord(char) > 31 and ord(char) <= 37:
            # Add the current character to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
