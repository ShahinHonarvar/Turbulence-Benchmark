
def filter_chars(string):
    new_string = ""
    for i in range(12, 89):
        if string[i] >= '&' and string[i] <= 'v':
            new_string += string[i]
    return new_string
