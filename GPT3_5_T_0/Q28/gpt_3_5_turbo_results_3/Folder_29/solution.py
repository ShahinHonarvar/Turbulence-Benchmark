def return_nth_smallest_ascii(s: str) -> str:
    s = s[5:10 + 1]
    if len(s) < 6:
        return ''

    s = sorted(s)
    return s[6 - 1]