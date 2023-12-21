def return_nth_smallest_ascii(s: str) -> str:
    s = s[25:77 + 1]
    if len(s) < 16:
        return ''

    s = sorted(s)
    return s[16 - 1]