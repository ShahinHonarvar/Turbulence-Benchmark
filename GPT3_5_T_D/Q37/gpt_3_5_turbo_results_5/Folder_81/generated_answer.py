
def filter_chars(string):
    filtered_string = ""
    for i in range(19, 93):
        if string[i] >= '8' and string[i] <= 'm':
            string = string.replace(string[i], "")
    return string
