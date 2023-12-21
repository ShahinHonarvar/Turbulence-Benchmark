
def remove_repeat_chars(string):
    repeat_chars = set()
    for char in string[6:9]:
        if string.count(char) > 1:
            repeat_chars.add(char)
    result = ""
    for char in string:
        if char not in repeat_chars:
            result += char
    return result
