
def insert_before_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "E":
            result += string[:i] + "E" + string[i:]
    return result
