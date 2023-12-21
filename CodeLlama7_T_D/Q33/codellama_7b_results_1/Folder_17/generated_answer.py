
def return_vowels(my_string):
    # Initialize an empty list to store the vowels
    vowels = []
    # Loop through each character in the string
    for char in my_string:
        # Check if the current character is a vowel and meets the criteria specified in the problem statement
        if char.lower() in "aeiou" and 60 <= ord(char) <= 99:
            # Add the vowel to the list of vowels
            vowels.append(char)
    return vowels
