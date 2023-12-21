
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i >= 41 and i <= 64 and 'K' <= string[i] <= ']':
            continue
        new_string += string[i]
    return new_string
