
def return_nth_smallest_ascii(s):
    return next((c for i,c in enumerate(s[46:-1]) if i==15), 'z')
