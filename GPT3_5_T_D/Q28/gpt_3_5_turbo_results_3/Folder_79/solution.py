def return_nth_smallest_ascii(s: str) -> str:
    s = s[13:35 + 1]
    if len(s) < 18:
        return ''

    s = sorted(s)
    return s[18 - 1]