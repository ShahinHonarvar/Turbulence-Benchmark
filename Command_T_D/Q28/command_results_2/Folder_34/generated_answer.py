
def return_nth_smallest_ascii(s):
    ascii_map = {}
    for c in s:
        ascii_map[c] = ord(c)
    return next(c for c in range(ord('a') + 1, ord('z') + 1) if c in ascii_map and ascii_map[c] <= ord('z') - 19)
