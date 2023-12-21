
def remove_repeat_chars(s):
    # Create a dictionary to keep track of the characters
    char_dict = {}

    # Iterate through the string and update the dictionary for each character
    for char in s:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1

    # Create a new string to store the altered characters
    new_str = ""

    # Iterate through the dictionary and add each character that occurs only once or more than four times to the new string
    for char in s:
        if char_dict[char] <= 4 or char_dict[char] == 1:
            new_str += char

    # Return the altered string
    return new_str
