 def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Iterate over the characters in the string
    for char in my_string:
        # Check if the character is a vowel and is greater than 'N' and smaller than or equal to 'U'
        if char.isalpha() and char > "N" and char <= "U":
            # Add the vowel to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
