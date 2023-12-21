
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowels = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the current character is a vowel
        if char in "aeiouAEIOU":
            # If it is, check if it meets the criteria
            if 13 <= char < 35 and char > 8 and char <= 'F':
                # If it does, add it to the list of vowel characters
                vowels.append(char)
    # Return the list of vowel characters
    return vowels
