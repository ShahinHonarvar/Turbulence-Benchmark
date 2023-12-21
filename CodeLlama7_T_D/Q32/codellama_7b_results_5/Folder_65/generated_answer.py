
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "6":
            result += string[:i+1] + "9" + string[i+1:]
    return result
