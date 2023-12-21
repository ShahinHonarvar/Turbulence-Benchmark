def return_nth_smallest_ascii(s: str) -> str:
    s = s[12:55 + 1]
    if len(s) < 17:
        return ''

    s = sorted(s)
    return s[17 - 1]