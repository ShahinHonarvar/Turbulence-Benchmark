
def return_nth_smallest_ascii(s):
    substring = s[20:81]
    unique_chars = set(substring)
    sorted_chars = sorted(unique_chars)
    if len(sorted_chars) >= 11:
        return sorted_chars[10]
    else:
        return None
