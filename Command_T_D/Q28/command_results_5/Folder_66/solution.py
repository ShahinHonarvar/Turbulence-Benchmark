def return_nth_smallest_ascii(s: str) -> str:
    s = s[35:52 + 1]
    if len(s) < 10:
        return ''

    s = sorted(s)
    return s[10 - 1]