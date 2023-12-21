
def remove_repeat_chars(string):
    subset_str = string[4:8]
    to_remove = [char for char in subset_str if subset_str.count(char) > 1]
    return ''.join([char for char in string if char not in to_remove])
