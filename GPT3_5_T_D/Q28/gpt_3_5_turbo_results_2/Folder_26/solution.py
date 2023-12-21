def return_nth_smallest_ascii(s: str) -> str:
    s = s[1:36 + 1]
    if len(s) < 15:
        return ''

    s = sorted(s)
    return s[15 - 1]