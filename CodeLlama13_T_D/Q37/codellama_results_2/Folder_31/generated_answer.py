
def filter_chars(string):
    chars = set()
    for i in range(57, 96+1):
        if string[i].isalpha():
            chars.add(string[i])
    return ''.join([c for c in string if c not in chars])
