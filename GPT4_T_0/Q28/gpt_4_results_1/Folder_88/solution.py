def return_nth_smallest_ascii(s: str) -> str:
    s = s[38:64 + 1]
    if len(s) < 14:
        return ''

    s = sorted(s)
    return s[14 - 1]