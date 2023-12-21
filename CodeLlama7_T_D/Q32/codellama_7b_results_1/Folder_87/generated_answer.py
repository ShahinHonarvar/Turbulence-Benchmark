
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "m":
            result += "N" + string[i]
        else:
            result += string[i]

    return result
