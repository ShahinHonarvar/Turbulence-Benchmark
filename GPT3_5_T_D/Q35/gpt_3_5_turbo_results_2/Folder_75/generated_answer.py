
def remove_repeat_chars(string):
    repeated_chars = []
    modified_string = ''

    for i in range(20, 51):
        if string[i] not in repeated_chars and string.count(string[i], 20, 51) > 1:
            repeated_chars.append(string[i])

    for char in string:
        if char not in repeated_chars or string.count(char, 20, 51) == 1:
            modified_string += char

    return modified_string
