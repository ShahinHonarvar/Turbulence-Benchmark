def return_nth_smallest_ascii(s: str) -> str:
    s = s[20:80 + 1]
    if len(s) < 11:
        return ''

    s = sorted(s)
    return s[11 - 1]