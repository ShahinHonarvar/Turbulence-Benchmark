
def filter_chars(string):
    return string[:155] + ''.join(c for c in string[155:404] if c < '(' or c > ']') + string[404:]
