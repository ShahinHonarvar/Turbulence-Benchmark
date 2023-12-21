
def filter_chars(string):
    result = ""
    for index, char in enumerate(string):
        if index < 63 or index >= 89 or char <= "*" or char >= "w":
            result += char
    return result
