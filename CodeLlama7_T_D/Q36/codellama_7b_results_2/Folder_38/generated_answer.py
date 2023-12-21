
def filter_chars(string):
    result = ""
    for i in range(44, 48):
        if string[i] > "+" and string[i] < "l":
            result += string[:i] + string[i+1:]
    return result
