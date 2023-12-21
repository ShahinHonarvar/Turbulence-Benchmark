
def filter_chars(string):
    filtered_string = ""
    for i in range(len(string)):
        if i < 3 or i >= 9 or string[i] <= "*" or string[i] >= "E":
            filtered_string += string[i]
    return filtered_string
