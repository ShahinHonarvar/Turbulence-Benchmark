
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if string[i] >= "H" and string[i] <= "e":
            continue
        result += string[i]
    return result
