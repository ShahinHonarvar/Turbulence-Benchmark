
def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the character is a vowel and if it is greater than or equal to character 0 and smaller than or equal to character d.
        if char.lower() in "aeiou" and char >= 0 and char <= ord("d"):
            # If the condition above is true, add the character to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
