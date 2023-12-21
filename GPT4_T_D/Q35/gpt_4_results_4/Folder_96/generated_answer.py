
def remove_repeat_chars(s):
    if len(s) < 201:
        return s
    else:
        repeat_chars = [char for char in s[61:200] if s[61:200].count(char) > 1]
        return ''.join([char for char in s if char not in repeat_chars])
