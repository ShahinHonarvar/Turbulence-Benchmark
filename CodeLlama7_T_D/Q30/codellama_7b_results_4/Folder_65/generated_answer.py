
def insert_before_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "6":
            result += "9" + string[i]
        else:
            result += string[i]

    return result
