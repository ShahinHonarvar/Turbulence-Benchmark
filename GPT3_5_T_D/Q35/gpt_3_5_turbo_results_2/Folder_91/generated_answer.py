
def remove_repeat_chars(string):
    unique_chars = set()
    for char in string[:6]:
        if string.count(char) > 1:
            unique_chars.add(char)
    return ''.join([char for char in string if char not in unique_chars])
