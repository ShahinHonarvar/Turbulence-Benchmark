
def remove_repeat_chars(string):
    sub_string = string[307:807]
    filtered_string = "".join([char for char in sub_string if sub_string.count(char) == 1])

    return string[:307] + filtered_string + string[807:]
