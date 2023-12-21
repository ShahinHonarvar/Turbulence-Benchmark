
def filter_chars(string):
    result = ""
    for i in range(138, 920+1):
        if string[i].isalpha() and string[i].lower() >= "6" and string[i].lower() <= "a":
            result += string[i]
    return result
