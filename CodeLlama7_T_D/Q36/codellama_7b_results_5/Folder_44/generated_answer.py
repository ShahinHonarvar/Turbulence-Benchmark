
def filter_chars(s):
    # Replace all characters between indices 18 and 64 with spaces
    s = s[:17] + " " * (len(s) - 17)
    return s
