
def filter_chars(string):
    chars = list(string)
    for i in range(82, 89):
        if chars[i] > '*' and chars[i] < '[':
            chars.remove(chars[i])
    return "".join(chars)
