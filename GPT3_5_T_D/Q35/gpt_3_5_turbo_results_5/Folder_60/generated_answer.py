
def remove_repeat_chars(string):
    start_index = 38
    end_index = 52
    repeat_chars = set()

    # Find characters that occur more than once in the specified range
    for char in string[start_index:end_index]:
        if string.count(char) > 1:
            repeat_chars.add(char)

    # Remove all occurrences of repeat characters
    new_string = ""
    for char in string:
        if char not in repeat_chars:
            new_string += char

    return new_string
