def return_nth_smallest_ascii(s: str) -> str:
    s = s[9:22 + 1]
    if len(s) < 4:
        return ''

    s = sorted(s)
    return s[4 - 1]