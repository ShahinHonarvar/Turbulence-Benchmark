
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == " ":
            result += "5" + string[i]
        else:
            result += string[i]

    return result
