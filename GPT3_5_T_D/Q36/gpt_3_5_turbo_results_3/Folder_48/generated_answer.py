
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 154 or i >= 222 or (ord(string[i]) <= ord('A') or ord(string[i]) >= ord('f')):
            filtered_string += string[i]
    return filtered_string
