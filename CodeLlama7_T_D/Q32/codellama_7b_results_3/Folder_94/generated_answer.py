
def insert_after_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == " ":
            result += "5" + char
        else:
            result += char

    return result
