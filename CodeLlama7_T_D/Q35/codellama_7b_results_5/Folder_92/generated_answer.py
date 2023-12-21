
def remove_repeat_chars(s):
    # Create a dictionary to keep track of characters and their indices
    char_indices = {}

    # Iterate over the characters in the string
    for i, char in enumerate(s):
        # If the character is already in the dictionary, add its index to the list
        if char in char_indices:
            char_indices[char].append(i)
        # Otherwise, create a new list with the current index
        else:
            char_indices[char] = [i]

    # Iterate over the characters in the string again
    for i, char in enumerate(s):
        # If the character is in the dictionary and has more than one index, remove all occurrences of that character from the string
        if char in char_indices and len(char_indices[char]) > 1:
            s = s[:i] + s[i+1:]

    # Return the altered string
    return s
