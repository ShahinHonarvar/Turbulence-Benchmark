
def insert_after_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == "U":
            result += f"F{char}"
        else:
            result += char

    return result
