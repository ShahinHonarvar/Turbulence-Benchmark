
def remove_repeat_chars(string):
    repeated_chars = set()
    for i in range(50, 92):
        char = string[i]
        if char in string[i+1:92] or char in string[50:i]:
            repeated_chars.add(char)
    return ''.join([char for char in string if char not in repeated_chars])
