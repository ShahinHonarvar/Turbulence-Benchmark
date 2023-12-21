
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "t":
            result += "tu"
        else:
            result += string[i]
    return result
