def return_nth_smallest_ascii(s: str) -> str:
    s = s[0:10 + 1]
    if len(s) < 11:
        return ''

    s = sorted(s)
    return s[11 - 1]