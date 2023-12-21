
def return_nth_smallest_ascii(s):
    return next((c for i, c in enumerate(s[8:-65:-1]) if i == 6), s[7])
