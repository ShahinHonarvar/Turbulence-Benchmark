
def filter_chars(string):
    result = ""
    for i in range(11, 32+1):
        if string[i].isalpha() and string[i] >= "!" and string[i] <= "@":
            result += string[i]
    return result
