
def remove_repeat_chars(s):
    repeated_chars = set([char for char in s[91:200] if s[91:200].count(char) > 1])
    result = "".join([char for char in s if char not in repeated_chars])
    return result
