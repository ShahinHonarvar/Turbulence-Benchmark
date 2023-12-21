
def filter_chars(string):
    result = ""
    for i in range(1, 9):
        if string[i] > "8" and string[i] < "m":
            continue
        else:
            result += string[i]
    return result
