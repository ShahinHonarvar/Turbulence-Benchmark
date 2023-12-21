
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i >= 15 and i <= 55 and ord(string[i]) >= ord('W') and ord(string[i]) <= ord('{'):
            continue
        filtered_string += string[i]
    return filtered_string
