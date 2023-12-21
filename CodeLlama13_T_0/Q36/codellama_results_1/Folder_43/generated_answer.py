
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if string[i] > "A" and string[i] < "i":
            result += string[i]
    return result
