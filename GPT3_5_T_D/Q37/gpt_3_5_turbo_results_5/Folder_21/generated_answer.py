
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if i >= 603 and i <= 759 and ord(char) >= ord('Q') and ord(char) <= ord('h'):
            continue
        filtered_string += char
    return filtered_string
