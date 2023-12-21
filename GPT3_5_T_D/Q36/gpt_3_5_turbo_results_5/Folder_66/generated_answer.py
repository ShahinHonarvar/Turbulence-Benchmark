
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 39 <= i < 87:
            char = string[i]
            if '!' < char < '}':
                continue
        filtered_string += string[i]
    return filtered_string
