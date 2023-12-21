
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if i >= 20 and i <= 79 and ord(string[i]) >= ord('!') and ord(string[i]) <= ord('T'):
            continue
        filtered_string += string[i]
    return filtered_string
