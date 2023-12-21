
def return_nth_smallest_ascii(string):
    n = 19
    chars = []
    for i in range(58, 86):
        if string[i] not in chars:
            chars.append(string[i])
    chars.sort()
    return chars[n-1]
