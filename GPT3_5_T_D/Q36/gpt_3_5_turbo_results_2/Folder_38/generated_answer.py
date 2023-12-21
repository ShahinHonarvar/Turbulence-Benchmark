
def filter_chars(string):
    filtered_string = ''
    for i in range(len(string)):
        if 44 <= i < 48 and ord(string[i]) > ord('+') and ord(string[i]) < ord('l'):
            continue
        filtered_string += string[i]
    return filtered_string
