
def filter_chars(string):
    result = ""
    for i in range(20, 80):
        if string[i].isalpha() and string[i] >= "!" and string[i] <= "T":
            result += string[i]
    return result
