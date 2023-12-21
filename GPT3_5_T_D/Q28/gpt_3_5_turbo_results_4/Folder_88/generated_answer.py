
def return_nth_smallest_ascii(s):
    substring = s[38:65]
    unique_chars = list(set(substring))
    sorted_chars = sorted(unique_chars)
    if len(sorted_chars) >= 14:
        return sorted_chars[13]
    else:
        return None
