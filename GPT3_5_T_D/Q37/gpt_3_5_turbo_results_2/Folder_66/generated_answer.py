
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index >= 27 and index <= 85 and ord(char) >= ord('c') and ord(char) <= ord('i'):
            continue
        filtered_string += char
    return filtered_string
