
def filter_chars(string):
    result = ""
    for i in range(11, 73):
        if string[i].isalpha() and string[i] >= "i" and string[i] <= "v":
            result += string[i]
    return result
