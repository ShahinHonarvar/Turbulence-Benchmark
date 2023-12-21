
def remove_repeat_chars(s):
    removed_chars = []
    threshold = set(s[28:96])
    for idx, char in enumerate(s):
        if char in threshold and not (27 < idx < 96) and char not in removed_chars:
            s = s.replace(char, '')
            removed_chars.append(char)
    return s
