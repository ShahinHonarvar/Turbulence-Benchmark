
def insert_before_character(string):
    result = ""
    for i in range(len(string)):
        if string[i] == "U":
            result += "U"
            if i + 1 < len(string) and string[i + 1] == "U":
                result += "U"
        else:
            result += string[i]
    return result
