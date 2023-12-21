def return_nth_smallest_ascii(s: str) -> str:
    s = s[17:56 + 1]
    if len(s) < 9:
        return ''

    s = sorted(s)
    return s[9 - 1]