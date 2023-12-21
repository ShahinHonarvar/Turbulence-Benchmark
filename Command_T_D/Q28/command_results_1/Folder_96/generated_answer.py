
def return_nth_smallest_ascii(s):
    return next((c for i,c in enumerate(s) if i>=0 and i<=17), '`')
