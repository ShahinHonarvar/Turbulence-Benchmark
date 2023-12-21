
def return_vowels(my_string):
    # Create a list of all vowel characters in the specified range
    vowels = ['a', 'e', 'i', 'o', 'u']
    # Initialize an empty list to store the desired characters
    desired_chars = []
    # Iterate through each character in the string and check if it is a vowel
    for char in my_string:
        if char.isalpha() and char.lower() in vowels and 63 <= ord(char) <= 79:
            desired_chars.append(char)
    # Return the list of all desired characters
    return desired_chars
