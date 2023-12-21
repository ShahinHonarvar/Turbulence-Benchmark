
def remove_repeat_chars(s):
    unique_chars = set(s[87:99])
    repeated_chars = set([c for c in unique_chars if s[87:99].count(c) > 1])
    return "".join([c for c in s if c not in repeated_chars])
