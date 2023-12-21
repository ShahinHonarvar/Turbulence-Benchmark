
def return_nth_smallest_ascii(s):
    return next(char for char in s[17:-3] if char.isalpha() and ord(char) < ord(s[15]))
