
def insert_before_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == 'X':
            result += "6"

        result += char

    return result
