
def filter_chars(input_string):
    for char in input_string[27:80]:
        if '>' > char > '<':
            input_string = input_string.replace(char, "")
    return input_string
