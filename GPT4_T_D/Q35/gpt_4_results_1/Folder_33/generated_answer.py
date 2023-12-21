
def remove_repeat_chars(s):
    chars = set()
    repeats = set()
    for i in range(126, 825):
        if s[i] in chars:
            repeats.add(s[i])
        else:
            chars.add(s[i])

    return ''.join([c for c in s if c not in repeats])
