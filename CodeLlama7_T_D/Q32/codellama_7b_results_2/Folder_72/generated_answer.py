
def insert_after_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == "O":
            result += "d" + char
        else:
            result += char

    return result
