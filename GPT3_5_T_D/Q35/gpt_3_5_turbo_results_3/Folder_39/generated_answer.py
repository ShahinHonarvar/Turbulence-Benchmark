
def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(45, 91):
        char = string[i]
        if char in string[44:91] and char not in repeated_chars:
            repeated_chars.add(char)
    return ''.join([char for char in string if char not in repeated_chars])
