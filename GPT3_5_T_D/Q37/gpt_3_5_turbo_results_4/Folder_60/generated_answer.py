
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 12 <= i <= 77 and ':' <= string[i] <= 'L':
            continue
        filtered_string += string[i]
    return filtered_string
