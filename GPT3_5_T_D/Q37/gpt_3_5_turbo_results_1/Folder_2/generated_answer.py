
def filter_chars(string):
    return ''.join([char for i, char in enumerate(string) if not ((i >= 477 and i <= 984) and char >= "," and char <= "V")])
