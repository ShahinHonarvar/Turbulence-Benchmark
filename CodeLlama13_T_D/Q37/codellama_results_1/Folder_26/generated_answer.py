
def filter_chars(string):
    result = ""
    for i in range(20, 63):
        if string[i].isalpha() and string[i] >= 'i' and string[i] <= 'k':
            result += string[i]
    return result
