
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if (11 <= i <= 32) and ('!' <= string[i] <= '@'):
            continue

        else:
            filtered_string += string[i]
    return filtered_string
