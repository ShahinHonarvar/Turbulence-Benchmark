
def filter_chars(string):
    result = ""
    for i, char in enumerate(string):
        if i < 39 or i > 87:
            result += char
        elif char > "!" and char < "}":
            result += char
    return result
