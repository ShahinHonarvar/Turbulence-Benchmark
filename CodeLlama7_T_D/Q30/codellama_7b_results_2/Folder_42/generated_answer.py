
def insert_before_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "O":
            result += "j"

        result += string[i]

    return result
