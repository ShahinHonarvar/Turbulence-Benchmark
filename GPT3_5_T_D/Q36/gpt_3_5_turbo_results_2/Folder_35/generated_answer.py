
def filter_chars(string):
    new_string = ""
    for i in range(len(string)):
        if i >= 163 and i < 658 and string[i] > '(' and string[i] < ']':
            continue
        else:
            new_string += string[i]
    return new_string
