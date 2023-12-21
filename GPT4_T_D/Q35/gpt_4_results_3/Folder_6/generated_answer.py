
def remove_repeat_chars(input_string):
    substring = input_string[21:93]
    for char in substring:
        if substring.count(char) > 1:
            input_string = input_string.replace(char, '')
    return input_string
