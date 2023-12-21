
def remove_repeat_chars(string):
    unique_chars = []
    altered_string = ""

    for i in range(51, 76):
        char = string[i]
        if char in unique_chars:
            continue
        unique_chars.append(char)

    for char in string:
        if char not in unique_chars:
            altered_string += char

    return altered_string
