
def filter_chars(input_string):
    for ch in input_string[67:90]:
        if '#' < ch < 'T':
            input_string = input_string.replace(ch, '')
    return input_string
