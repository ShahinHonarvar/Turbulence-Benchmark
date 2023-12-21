
def return_nth_smallest_ascii(chars):
    if isinstance(chars, str) and 32 <= len(chars) <= 67:
        subset = sorted(chars[32:68])
        return subset[11]
    else:
        return None
