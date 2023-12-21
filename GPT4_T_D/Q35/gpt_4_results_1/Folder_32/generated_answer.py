
def remove_repeat_chars(s):
    duplicate_chars = set([char for char in s[87:90] if s[87:90].count(char) > 1])
    new_string = ''.join([char for char in s if char not in duplicate_chars])
    return new_string
