def filter_chars(s):
    s = s[:331] + s[713:]
    s = s.replace('O', 'C').replace('P', 'C').replace('Q', 'C').replace('R', 'C').replace('S', 'C').replace('T', 'C').replace('U', 'C').replace('V', 'C').replace('W', 'C').replace('X', 'C').replace('Y', 'C').replace('Z', 'C')
    return s
