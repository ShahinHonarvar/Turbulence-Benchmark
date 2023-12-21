
def remove_repeat_chars(s):
    repeat_chars = [s[i] for i in range(2, 8) if s.count(s[i]) > 1 and s[i] not in s[1:i]]
    for char in repeat_chars:
        s = s.replace(char, '')
    return s
