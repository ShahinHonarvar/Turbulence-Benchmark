
def remove_repeat_chars(string):
    repeated_chars = []
    altered_string = ""
    for index, char in enumerate(string):
        if index > 73 and index < 84:
            if char not in repeated_chars and string.count(char) > 1:
                repeated_chars.append(char)
            elif char in repeated_chars:
                continue
        altered_string += char
    return altered_string
