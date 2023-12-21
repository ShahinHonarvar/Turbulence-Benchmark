
def filter_chars(string):
    return string[:42] + ''.join([char for char in string[42:78] if char <= '?' and char > '!']) + string[78:]
