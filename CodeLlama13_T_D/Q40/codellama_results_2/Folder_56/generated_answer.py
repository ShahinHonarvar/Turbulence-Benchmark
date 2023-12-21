
def return_n_smallest_chars(s):
    chars = []
    for char in s:
        if char not in chars:
            chars.append(char)
    chars.sort()
    return chars[:21]
