
def filter_chars(input_string):
    filter_chars = set([c for c in input_string[319:337] if 'B' < c < 'z'])
    for c in input_string:
        if c in filter_chars:
            input_string = input_string.replace(c,'')
    return input_string
