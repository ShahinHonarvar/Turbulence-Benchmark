
def filter_chars(string):
    start = 69
    end = 97
    new_string = ""
    for i, char in enumerate(string):
        if start <= i < end and "V" < char < "j":
            continue
        new_string += char
    return new_string
