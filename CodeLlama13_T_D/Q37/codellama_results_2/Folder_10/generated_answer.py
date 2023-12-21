
def filter_chars(string):
    result = ""
    for i in range(63, 84 + 1):
        if string[i] >= "E" and string[i] <= "~":
            result += string[i]
    return result
