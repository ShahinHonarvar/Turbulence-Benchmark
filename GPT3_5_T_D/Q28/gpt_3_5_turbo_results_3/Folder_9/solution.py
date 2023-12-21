def return_nth_smallest_ascii(s: str) -> str:
    s = s[10:90 + 1]
    if len(s) < 20:
        return ''

    s = sorted(s)
    return s[20 - 1]