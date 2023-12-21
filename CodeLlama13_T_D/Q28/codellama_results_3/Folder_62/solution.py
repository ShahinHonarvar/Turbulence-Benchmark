def return_nth_smallest_ascii(s: str) -> str:
    s = s[51:78 + 1]
    if len(s) < 9:
        return ''

    s = sorted(s)
    return s[9 - 1]