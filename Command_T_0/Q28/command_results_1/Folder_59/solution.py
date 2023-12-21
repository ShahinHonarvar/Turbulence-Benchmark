def return_nth_smallest_ascii(s: str) -> str:
    s = s[0:11 + 1]
    if len(s) < 12:
        return ''

    s = sorted(s)
    return s[12 - 1]