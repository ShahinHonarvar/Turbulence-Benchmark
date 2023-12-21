
def remove_repeat_chars(string):
    # Create a dictionary to store the frequency of each character
    char_freq = {}
    for char in string:
        if char not in char_freq:
            char_freq[char] = 1
        else:
            char_freq[char] += 1
    # Iterate over the characters in the string and remove any duplicates
    new_string = ""
    for i, char in enumerate(string):
        if char_freq[char] > 1:
            # If the character is repeated, remove all instances of it from the string
            new_string += string[i + 1:]
            break

        else:

            # Add the character to the new string and continue iterating over the characters
            new_string += char

    return new_string
