
def filter_chars(s):
    new_string = ''
    for i, c in enumerate(s[669:888]):
        if ord(c) > ord('B') and ord(c) < ord('Y'):
            continue
        else:
            new_string += c
    return s[:669] + new_string + s[888:]
