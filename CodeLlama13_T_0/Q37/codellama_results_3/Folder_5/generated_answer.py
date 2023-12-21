
def filter_chars(string):
    result = ""
    for i in range(24, 83):
        if string[i].isdigit() and int(string[i]) >= 5 and int(string[i]) <= 9:
            result += string[i]
    return result
