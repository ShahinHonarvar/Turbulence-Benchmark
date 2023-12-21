
def filter_chars(s):
    chars = []
    for i, c in enumerate(s):
        if 69 <= ord(c) <= 97 and c < 'j' and c > 'V':
            continue
        else:
            chars.append(c)
    return "".join(chars)
