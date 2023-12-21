
def remove_repeat_chars(s):
    part = s[34:78]
    new_s = list(s)
    for char in set(part):
        if part.count(char) > 1:
            while char in new_s:
                new_s.remove(char)
    return ''.join(new_s)
