
def return_n_smallest_chars(string):
    chars = []
    for char in string:
        if char not in chars:
            chars.append(char)
    chars.sort()
    return chars[0:23]
