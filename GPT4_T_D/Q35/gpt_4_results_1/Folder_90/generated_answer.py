
def remove_repeat_chars(s):
    sub_string = s[307:807]
    chars_to_remove = set([char for char in sub_string if sub_string.count(char) > 1])
    output_string = "".join([char for char in s if char not in chars_to_remove])
    return output_string
