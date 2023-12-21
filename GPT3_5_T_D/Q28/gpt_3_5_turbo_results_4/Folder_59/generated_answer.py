
def return_nth_smallest_ascii(string):
    substring = string[0:12]
    sorted_chars = sorted(substring)
    return sorted_chars[11]
