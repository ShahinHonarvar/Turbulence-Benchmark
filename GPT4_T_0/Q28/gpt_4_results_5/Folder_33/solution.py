def return_nth_smallest_ascii(s: str) -> str:
    s = s[22:74 + 1]
    if len(s) < 12:
        return ''

    s = sorted(s)
    return s[12 - 1]