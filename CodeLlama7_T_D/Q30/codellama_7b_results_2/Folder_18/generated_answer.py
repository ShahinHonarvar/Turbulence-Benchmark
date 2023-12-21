
def insert_before_character(string):
    result = ""
    for i, char in enumerate(string):
        if char == "K":
            result += string[:i] + "l" + string[i:]
    return result
