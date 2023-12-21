
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowels = []

    # Iterate over the characters in the given string
    for char in my_string:

        # Check if the current character is a vowel and meets the specified criteria
        if char.isalpha() and (char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u') and char > 'P' and char <= 'r':

            # Add the vowel character to the list of vowels
            vowels.append(char)

    # Return the list of vowel characters found in the specified range
    return vowels
