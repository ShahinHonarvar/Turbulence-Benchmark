
def filter_chars(string):
    filtered_string = ""
    for i, char in enumerate(string):
        if 770 <= i <= 970 and ord('-') <= ord(char) <= ord('D'):
            filtered_string += char
    return filtered_string
