
def insert_after_character(s):
    t = ''
    for c in s:
        t += c
        if c == 'a':
            t += 'n'
    return t
