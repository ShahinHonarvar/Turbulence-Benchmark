
def filter_chars(s):
    # Remove all occurrences of characters between 63 and 89 (both exclusive)
    for i in range(63, 89):
        s = s.replace(chr(i), '')
    return s
