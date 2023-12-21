
def filter_chars(string):
    chars = list(string)
    for i in range(477, 985):
        if chars[i].isalpha() and chars[i].lower() >= ',' and chars[i].lower() <= 'v':
            chars.remove(chars[i])
    return "".join(chars)
