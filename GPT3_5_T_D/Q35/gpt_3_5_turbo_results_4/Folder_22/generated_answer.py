
def remove_repeat_chars(string):
    indices = set()
    for i in range(50, 200):
        if string[i] in indices:
            string = string.replace(string[i], "")
        else:
            indices.add(string[i])
    return string
