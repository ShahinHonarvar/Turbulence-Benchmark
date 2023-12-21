
def remove_repeat_chars(string):
    sub_string = string[307:807]
    unique_chars = set(sub_string)
    for char in unique_chars:
        if sub_string.count(char) > 1:
            string = string.replace(char, '')
    return string
