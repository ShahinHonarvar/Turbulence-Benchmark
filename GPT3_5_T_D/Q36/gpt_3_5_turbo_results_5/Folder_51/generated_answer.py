
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i >= 58 and i < 81 and string[i] > '5' and string[i] < '>':
            continue
        else:
            new_string += string[i]
    return new_string
