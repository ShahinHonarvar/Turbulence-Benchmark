
def return_nth_smallest_ascii(s):
    return next((c for i, c in enumerate(sorted(s[51:78]) + [x for x in s if x < ord('z')]) if i == 9), 'z')
