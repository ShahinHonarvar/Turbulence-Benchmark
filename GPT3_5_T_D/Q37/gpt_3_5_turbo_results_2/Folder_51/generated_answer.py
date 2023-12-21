
def filter_chars(string):
    final_string = ''
    for index, char in enumerate(string):
        if 36 <= index <= 40 and 'H' <= char <= 'e':
            continue
        final_string += char
    return final_string
