
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "g":
            result += string[:i] + "M" + string[i:]
    return result
