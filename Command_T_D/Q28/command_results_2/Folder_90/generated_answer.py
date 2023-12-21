
def return_nth_smallest_ascii(s):
    return next(i for i in s[17:-83] if i in "qwertyuiopasdfghjklzxcvbnm")
