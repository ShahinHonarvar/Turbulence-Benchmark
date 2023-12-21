 def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []
    # Loop through the characters in the specified range
    for char in my_string[529:828]:
        # Check if the current character is a vowel
        if char in "aeiouAEIOU":
            # Add the current character to the list of vowels
            vowel_list.append(char)
    # Return the list of vowel characters
    return vowel_list
