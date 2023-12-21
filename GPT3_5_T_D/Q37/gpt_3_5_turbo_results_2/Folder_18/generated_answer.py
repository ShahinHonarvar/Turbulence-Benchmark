
def filter_chars(string):
    filtered_string = ""
    for index, char in enumerate(string):
        if index < 770 or index > 970 or char < '-' or char > 'D':
            filtered_string += char
    return filtered_string
