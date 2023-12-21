
def remove_repeat_chars(s):
    # Initialize a dictionary to keep track of characters
    char_dict = {}

    # Iterate over each character in the string
    for char in s:

        # If the character is already in the dictionary, increment its count
        if char in char_dict:
            char_dict[char] += 1

        # Otherwise, add the character to the dictionary with a count of 1
        else:
            char_dict[char] = 1

    # Iterate over each key-value pair in the dictionary
    for key, value in char_dict.items():

        # If the count of the character is greater than 1, remove all occurrences of that character from the string
        if value > 1:
            s = s.replace(key, '')

    return s
