
def remove_repeat_chars(s):
    seen = {}
    for i, ch in enumerate(s):
        if 10 < i < 79:
            if ch in seen:
                s = s.replace(ch, '')
            else:
                seen[ch] = True
    return s
