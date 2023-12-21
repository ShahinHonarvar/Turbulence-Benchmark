
def return_nth_smallest_ascii(s):
    return next(c for i,c in enumerate(s[13:35]) if ord(c)<=ord(s[i-1])+17)
