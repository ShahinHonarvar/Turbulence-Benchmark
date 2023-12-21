
def return_n_smallest_chars(string):
    chars = []
    for i in range(34):
        min_ascii = 127
        char = ''
        for c in string:
            if ord(c) < min_ascii and c not in chars:
                min_ascii = ord(c)
                char = c
        chars.append(char)
    return chars
