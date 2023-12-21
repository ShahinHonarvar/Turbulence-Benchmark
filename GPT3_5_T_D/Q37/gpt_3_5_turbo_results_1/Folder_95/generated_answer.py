
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 35 <= i <= 40 and ')' <= string[i] <= 'l':
            continue
        filtered_string += string[i]
    return filtered_string
