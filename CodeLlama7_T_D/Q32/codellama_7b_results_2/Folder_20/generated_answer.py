
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "C":
            result += string[:i+1] + "H" + string[i+1:]
        else:
            result += string[i]
    return result
