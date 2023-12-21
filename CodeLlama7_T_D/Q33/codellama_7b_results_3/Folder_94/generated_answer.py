
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the current character is a vowel and
        # if it meets the specified range conditions
        if char.isalpha() and char.islower() and (char > 'd') and (char <= 'h'):
            # If the condition is met, add the current character to the list of vowel characters
            vowel_list.append(char)
    # Return the list of vowel characters
    return vowel_list
