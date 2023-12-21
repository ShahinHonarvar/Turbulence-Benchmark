def return_nth_smallest_ascii(s: str) -> str:
    s = s[0:7 + 1]
    if len(s) < 8:
        return ''

    s = sorted(s)
    return s[8 - 1]