
def filter_chars(string):
    altered_string = ''
    for i in range(len(string)):
        if i < 318 or i >= 337:
            altered_string += string[i]
        elif string[i] > 'B' and string[i] < 'z':
            continue
        else:
            altered_string += string[i]
    return altered_string
