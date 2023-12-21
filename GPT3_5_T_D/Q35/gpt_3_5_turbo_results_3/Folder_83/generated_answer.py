
def remove_repeat_chars(string):
    repeat_chars = set()
    for i in range(100, 200):
        if string.count(string[i]) > 1:
            repeat_chars.add(string[i])
    result = ""
    for char in string:
        if char not in repeat_chars:
            result += char
    return result
