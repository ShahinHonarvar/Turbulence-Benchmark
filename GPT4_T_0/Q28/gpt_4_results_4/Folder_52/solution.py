def return_nth_smallest_ascii(s: str) -> str:
    s = s[46:72 + 1]
    if len(s) < 15:
        return ''

    s = sorted(s)
    return s[15 - 1]