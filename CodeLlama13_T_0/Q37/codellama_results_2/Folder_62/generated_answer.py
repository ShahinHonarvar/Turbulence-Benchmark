
def filter_chars(string):
    result = ""
    for i in range(10, 70):
        if string[i].isalpha() and string[i] >= "I" and string[i] <= "K":
            result += string[i]
    return result
