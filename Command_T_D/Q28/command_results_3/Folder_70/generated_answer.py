
def return_nth_smallest_ascii(s):
    return next((x for x in s[28:-2] if ord(x) == s[28:-2].index(min(s[28:-2]))), None)
