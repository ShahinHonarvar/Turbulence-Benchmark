
def remove_repeat_chars(s):
    repeat_chars = [i for i in set(s[10:28]) if s[10:28].count(i) > 1]
    for char in repeat_chars:
        s = s.replace(char, "")
    return s
