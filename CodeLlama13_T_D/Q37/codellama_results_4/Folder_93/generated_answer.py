
def filter_chars(string):
    chars = set()
    for i in range(38, 69 + 1):
        if string[i] >= 'H' and string[i] <= 'e':
            chars.add(string[i])
    return ''.join([c for c in string if c not in chars])
