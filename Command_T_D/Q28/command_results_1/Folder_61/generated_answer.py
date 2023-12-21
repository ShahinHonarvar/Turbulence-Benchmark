
def return_nth_smallest_ascii(s):
    return next((c for c in s if ord(c) < 10), 'A')
