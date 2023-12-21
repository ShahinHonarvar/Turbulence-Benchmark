
def filter_chars(string):
    return string[:155] + ''.join(char for char in string[155:404] if not ('(' <= char <= ']')) + string[404:]
