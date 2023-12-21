
def return_nth_smallest_ascii(s):
    s_sub = s[52:80]
    sorted_chars = sorted(s_sub, key = lambda x : ord(x))
    return sorted_chars[6] if len(sorted_chars) > 6 else None
