
def remove_repeat_chars(string):
    result = ""
    for i, char in enumerate(string):
        if 125 < i < 825:
            if string[125:825].count(char) < 2:
                result += char
        else:
            result += char
    return result
