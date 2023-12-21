
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if 61 <= i <= 70 and '0' <= string[i] <= '@':
            continue
        filtered_string += string[i]
    return filtered_string
