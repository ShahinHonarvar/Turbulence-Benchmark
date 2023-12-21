 def return_vowels(string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Iterate through each character in the string
    for char in string:
        # Check if the character is a vowel and is greater than the specified character % and smaller than or equal to character G
        if char.isalpha() and (char > "%" and char <= "G"):
            # Add the vowel to the list of vowels
            vowels.append(char)
    return vowels
