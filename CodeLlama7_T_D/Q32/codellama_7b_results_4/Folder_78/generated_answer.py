
def insert_after_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == "H":
            result += char + "s"
        else:
            result += char

    return result
