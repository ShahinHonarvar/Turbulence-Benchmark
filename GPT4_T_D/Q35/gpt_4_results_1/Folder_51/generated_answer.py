
def remove_repeat_chars(string):
    exclusive_area = set(string[7:9])
    repeat_chars = exclusive_area.intersection(set([char for char in string if string.count(char) > 1]))
    return ''.join([char for char in string if char not in repeat_chars])
