
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if (i < 55 or i > 80) and string[i].isalpha() and string[i].lower() != 's':
            result += string[i]
    return result
