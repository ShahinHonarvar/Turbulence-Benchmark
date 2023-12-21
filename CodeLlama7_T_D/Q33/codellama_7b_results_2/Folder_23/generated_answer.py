
def return_vowels(string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through each character in the string
    for char in string:
        # Check if the current character is a vowel and its index is between 56 and 96
        if char.isalpha() and (char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u') and 56 <= string.index(char) < 96:
            # If the current character meets the above condition, add it to the list of vowels
            vowels.append(char)
    # Return the list of vowels
    return vowels
