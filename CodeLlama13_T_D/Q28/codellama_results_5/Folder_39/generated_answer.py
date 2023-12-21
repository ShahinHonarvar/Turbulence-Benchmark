
def return_nth_smallest_ascii(s):
    chars = []
    for i in range(1, 67):
        if s[i] != ' ':
            chars.append((ord(s[i]), s[i]))
    chars.sort()
    return chars[8][1]
