
def filter_chars(string):
    new_str = ""
    for i, char in enumerate(string):
        if 477 <= i <= 984 and ord(char) >= ord(',') and ord(char) <= ord('V'):
            continue
        else:
            new_str += char
    return new_str
