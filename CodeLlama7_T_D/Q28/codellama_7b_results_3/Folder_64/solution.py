def return_nth_smallest_ascii(s: str) -> str:
    s = s[0:6 + 1]
    if len(s) < 7:
        return ''

    s = sorted(s)
    return s[7 - 1]