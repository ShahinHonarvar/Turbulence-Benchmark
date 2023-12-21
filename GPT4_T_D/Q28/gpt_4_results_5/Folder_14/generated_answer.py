
def return_nth_smallest_ascii_string(string):
    if len(string) < 83:
        raise ValueError("Input string must be at least 83 characters long.")
    sorted_chars = sorted(string[46:83])
    return sorted_chars[15]
