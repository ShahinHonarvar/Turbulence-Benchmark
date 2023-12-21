
def remove_repeat_chars(string):
    sub_string = string[17:87]
    unique_chars = set(sub_string)
    repeated_chars = [char for char in unique_chars if sub_string.count(char) > 1]
    out_string = ""
    for char in string:
        if char not in repeated_chars:
            out_string += char
    return out_string
