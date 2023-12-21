
def filter_chars(input_string):
    if len(input_string) < 80:
        temp_string = input_string
    else:
        temp_string = input_string[24:80]

    for char in temp_string:
        if 'a' <= char <= 'f':
            input_string = input_string.replace(char, "")

    return input_string
