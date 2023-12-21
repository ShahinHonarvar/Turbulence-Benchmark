
def insert_after_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "2":
            result += "S" + string[i + 1:]
            break

    return result
