
def filter_chars(string):
    result = ""
    for i in range(len(string)):
        if string[i].isalpha() and string[i] >= "R" and string[i] <= "t":
            result += string[i]
    return result
