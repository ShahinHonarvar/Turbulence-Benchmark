 def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []
    # Iterate through the characters in the string
    for char in my_string:
        # Check if the character is a vowel and is greater than character N and smaller than or equal to character W
        if char.isalpha() and (char > 'N' and char <= 'W'):
            # Add the character to the list of vowel characters
            vowel_list.append(char)
    # Return the list of vowel characters
    return vowel_list
