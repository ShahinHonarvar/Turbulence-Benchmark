def return_nth_smallest_ascii(s: str) -> str:
    s = s[1:46 + 1]
    if len(s) < 13:
        return ''

    s = sorted(s)
    return s[13 - 1]