
def remove_repeat_chars(s):
    piece = s[82:86]
    for char in set(piece):
        if piece.count(char) > 1:
            s = s.replace(char, '')
    return s
