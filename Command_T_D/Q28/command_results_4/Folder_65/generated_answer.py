
def return_nth_smallest_ascii(s):
    return next(char for char in s[32:67] if ord(char) == 12)
