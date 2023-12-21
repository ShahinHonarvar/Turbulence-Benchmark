
def filter_chars(string):
    new_string = ""
    for char in string:
        if ord(char) >= 722 and ord(char) <= 832 and ord(char) >= ord('K') and ord(char) <= ord('m'):
            continue
        else:
            new_string += char
    return new_string
