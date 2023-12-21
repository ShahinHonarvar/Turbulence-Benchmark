
def filter_chars(s):
    filtered = [ch for ch in s[332:713] if ch <= 'M' or ch >= '_']
    return s[:332] + "".join(filtered) + s[713:]
