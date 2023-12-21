
def return_nth_smallest_ascii(s):
    ascii_lower = 'z'
    ascii_upper = 'z'
    for i in range(len(s)):
        if s[i] in ascii_lower:
            ascii_lower = s[i]
        elif s[i] in ascii_upper:
            ascii_upper = s[i]
    return ascii_lower if ascii_lower in ascii_upper else ascii_upper
