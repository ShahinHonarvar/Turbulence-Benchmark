
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if 31 < index < 50 and ord(char) > ord('/') and ord(char) < ord('J'):
            continue
        filtered_string += char
    return filtered_string
