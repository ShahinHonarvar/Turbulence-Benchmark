
def return_nth_smallest_ascii(s):
    chars = sorted(list(s[34:86]))
    if len(chars) >= 20:
        return chars[19]
    else:
        return None
