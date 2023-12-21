def return_nth_smallest_ascii(s: str) -> str:
    s = s[14:35 + 1]
    if len(s) < 11:
        return ''

    s = sorted(s)
    return s[11 - 1]