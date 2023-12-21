
def remove_repeat_chars(s):
    # Find the indices of the characters that occur more than once between the specified indices
    start_index = 86
    end_index = 99
    repeated_chars = []
    for i in range(start_index, end_index):
        if s[i] not in repeated_chars:
            repeated_chars.append(s[i])
    # Remove all occurrences of the repeated characters from the string
    new_string = ""
    for char in s:
        if char not in repeated_chars:
            new_string += char

    return new_string
