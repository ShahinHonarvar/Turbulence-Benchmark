
def remove_repeat_chars(string):
    repeat_chars = set()
    for char in string[60:200]:
        if string[60:200].count(char) > 1:
            repeat_chars.add(char)
    return ''.join([char for char in string if char not in repeat_chars])
