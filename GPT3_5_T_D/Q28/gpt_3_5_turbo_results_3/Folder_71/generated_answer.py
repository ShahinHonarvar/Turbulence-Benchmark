
def return_nth_smallest_ascii(s):
    chars = sorted(s[5:83])
    if len(chars) < 16:
        return None
    return chars[15]
