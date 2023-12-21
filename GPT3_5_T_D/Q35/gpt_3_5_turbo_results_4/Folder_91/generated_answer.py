
def remove_repeat_chars(string):
    non_repeated_chars = []
    for i in range(6): 
        if string[i] not in non_repeated_chars and string.count(string[i]) == 1:
            non_repeated_chars.append(string[i])
    return ''.join([char for char in string if char in non_repeated_chars or string.index(char) < 6])
