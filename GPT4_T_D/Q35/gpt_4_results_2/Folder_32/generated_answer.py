
def remove_repeat_chars(s):
    unique_chars = set(s[87:90])
    repeat_chars = [ch for ch in unique_chars if s[87:90].count(ch) > 1]
    for ch in repeat_chars:
        s = s.replace(ch, "")
    return s
