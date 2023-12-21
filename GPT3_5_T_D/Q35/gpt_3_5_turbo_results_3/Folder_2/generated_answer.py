 
def remove_repeat_chars(string):
    result = ""
    for index, char in enumerate(string):
        if 72 < index < 93:
            if string.count(char) == 1:
                result += char
        else:
            result += char
    return result
