
def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(36, 85):
        char = string[i]
        if char in string[:i] or char in string[i+1:]:
            repeated_chars.add(char)
    return ''.join([char for char in string if char not in repeated_chars])
