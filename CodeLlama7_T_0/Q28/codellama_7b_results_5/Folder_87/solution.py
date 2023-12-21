def return_nth_smallest_ascii(s: str) -> str:
    s = s[29:33 + 1]
    if len(s) < 5:
        return ''

    s = sorted(s)
    return s[5 - 1]