
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i >= 138 and i <= 920 and string[i] >= '6' and string[i] <= 'A':
            continue
        new_string += string[i]
    return new_string
