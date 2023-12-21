
def remove_repeat_chars(string):
    repeat_chars = set()
    result = []
    for index, char in enumerate(string):
        if 60 < index < 200 and string.count(char) > 1:
            repeat_chars.add(char)
        elif char not in repeat_chars:
            result.append(char)
    return "".join(result)
