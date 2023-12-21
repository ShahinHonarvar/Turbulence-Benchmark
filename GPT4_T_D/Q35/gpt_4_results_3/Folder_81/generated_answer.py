
def remove_repeat_chars(s):
    if len(s) < 201:
        return s
    else:
        to_remove = [char for char in s[21:200] if s[21:200].count(char) > 1]
        return "".join([char for char in s if char not in to_remove])
