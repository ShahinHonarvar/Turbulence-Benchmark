
def insert_after_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == "U":
            result += char + "U"
        else:
            result += char

    return result
