
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []
    # Iterate through the characters in the string
    for char in my_string:
        # Check if the character is a vowel and if it's greater than L and smaller than or equal to d
        if char.lower() in "aeiou" and ord(char) > ord("L") and ord(char) <= ord("d"):
            # If the condition is true, add the character to the list of vowel characters
            vowel_list.append(char)
    # Return the list of vowel characters
    return vowel_list
