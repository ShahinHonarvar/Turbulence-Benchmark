
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 344 or i >= 874:
            filtered_string += string[i]
        elif ord(string[i]) <= ord('f') or ord(string[i]) >= ord('~'):
            filtered_string += string[i]
    return filtered_string
