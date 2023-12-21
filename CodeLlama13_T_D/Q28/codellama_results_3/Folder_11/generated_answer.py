
def return_nth_smallest_ascii(s):
    chars = []
    for i in range(9, 60):
        if s[i] != ' ' and s[i] not in chars:
            chars.append(s[i])
    return chr(sorted(chars)[5])
