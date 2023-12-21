
def insert_after_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == "g":
            result += "M" + char
        else:
            result += char

    return result
