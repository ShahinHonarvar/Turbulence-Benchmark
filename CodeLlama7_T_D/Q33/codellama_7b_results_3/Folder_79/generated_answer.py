
def return_vowels(my_string):
    # Initialize an empty list to store the vowel characters
    vowel_list = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the character is a vowel and if it is between index 74 (inclusive) and index 96 (exclusive)
        if char.isalpha() and (char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u') and 74 <= my_string.index(char) <= 96:
            # If the character is a vowel and between the specified indices, add it to the list of vowel characters
            vowel_list.append(char)
    # Return the list of vowel characters
    return vowel_list
