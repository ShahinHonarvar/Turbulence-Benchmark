
def filter_chars(input):
    for ch in input[172:636]:
        if 'c' < ch < 's':
            input = input.replace(ch, '')
    return input
