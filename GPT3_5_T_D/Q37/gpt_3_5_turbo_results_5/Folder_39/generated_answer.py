
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 52 or i > 81 or not ('A' <= string[i] <= 'U'):
            filtered_string += string[i]
    return filtered_string
