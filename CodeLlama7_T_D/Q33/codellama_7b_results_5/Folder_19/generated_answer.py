
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowels = []
    # Iterate through the characters in the string
    for i in range(51, 78):
        # Check if the current character is a vowel
        if my_string[i] in "aeiou":
            # If it is, add it to the list of vowels
            vowels.append(my_string[i])
    # Return the list of vowels
    return vowels
