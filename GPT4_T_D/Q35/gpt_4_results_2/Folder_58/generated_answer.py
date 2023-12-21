
def remove_repeat_chars(s):
    subset = s[104:802]
    repeat_chars = [char for char in subset if subset.count(char) > 1]
    output = ''.join([char for char in s if char not in repeat_chars])
    return output
