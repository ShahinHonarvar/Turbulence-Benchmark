
def remove_repeat_chars(s):
    to_remove = [char for char in s[91:200] if s[91:200].count(char)>1]
    new_s = ''.join([char for char in s if char not in to_remove])
    return new_s
