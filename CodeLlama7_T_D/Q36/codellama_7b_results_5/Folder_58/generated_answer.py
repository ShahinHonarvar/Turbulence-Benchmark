
def filter_chars(string):
    result = ""
    for i in range(318, 337):
        if string[i] > "B" and string[i] < "z":
            result += string[:i] + string[i+1:]
    return result
