
def filter_chars(string):
    filtered_string = ''
    for i, char in enumerate(string):
        if i >= 83 and i <= 99 and ord(char) >= ord('*') and ord(char) <= ord('j'):
            continue
        filtered_string += char
    return filtered_string
