
def remove_repeat_chars(string):
    indices = set()
    for i in range(70, 200):
        if string.count(string[i]) > 1:
            indices.add(i)
    result = ''
    for i, char in enumerate(string):
        if i not in indices:
            result += char
    return result
