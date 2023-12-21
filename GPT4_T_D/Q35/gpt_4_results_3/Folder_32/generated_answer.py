
def remove_repeat_chars(s):
    target_chars = [char for char in s[87:90] if s[87:90].count(char) > 1]
    for char in target_chars:
        s = s.replace(char, '')
    return s
