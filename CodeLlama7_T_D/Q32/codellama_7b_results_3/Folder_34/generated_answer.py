
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i].upper() == "A":
            result += string[:i+1] + "a" + string[i+1:]
    return result
