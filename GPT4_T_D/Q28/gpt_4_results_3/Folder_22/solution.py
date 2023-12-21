def return_nth_smallest_ascii(s: str) -> str:
    s = s[0:16 + 1]
    if len(s) < 17:
        return ''

    s = sorted(s)
    return s[17 - 1]