
def filter_chars(string):
    filtered_str = ""
    for char in string:
        if ord(char) < 73 or ord(char) > 74:
            continue
        elif ord(char) >= 85 and ord(char) <= 122:
            filtered_str += char
        else:
            pass
    return filtered_str
