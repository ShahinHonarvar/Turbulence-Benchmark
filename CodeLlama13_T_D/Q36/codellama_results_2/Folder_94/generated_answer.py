
def filter_chars(string):
    result = ""
    for i in range(15, 85):
        if string[i].lower() >= 'i' and string[i].lower() < 'm':
            result += string[i]
    return result
