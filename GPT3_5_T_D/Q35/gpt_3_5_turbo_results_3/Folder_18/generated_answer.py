
def remove_repeat_chars(string):
    unique_chars = []
    new_string = ""

    for char in string:
        if char not in unique_chars:
            unique_chars.append(char)
            new_string += char
        elif 56 < string.index(char) < 90:
            new_string = new_string.replace(char, "")

    return new_string
