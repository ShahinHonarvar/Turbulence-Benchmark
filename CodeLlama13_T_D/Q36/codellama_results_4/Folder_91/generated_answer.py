
def filter_chars(string):
    chars = []
    for i in range(4):
        if string[i] > '$' and string[i] < '?':
            chars.append(string[i])
    return "".join(chars)
