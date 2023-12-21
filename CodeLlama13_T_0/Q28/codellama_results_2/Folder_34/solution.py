def return_nth_smallest_ascii(s: str) -> str:
    s = s[0:18 + 1]
    if len(s) < 19:
        return ''

    s = sorted(s)
    return s[19 - 1]