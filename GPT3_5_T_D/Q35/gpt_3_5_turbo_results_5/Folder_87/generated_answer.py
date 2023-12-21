
def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(21, 43):
        char = string[i]
        if string.count(char, 21, 43) > 1:
            repeated_chars.add(char)

    return ''.join([char for char in string if char not in repeated_chars])
