
def filter_chars(my_string):
    char_to_remove = set(my_string[138:921]).intersection(set([chr(i) for i in range(ord('6'), ord('A') + 1)]))
    return ''.join([char for char in my_string if char not in char_to_remove])
