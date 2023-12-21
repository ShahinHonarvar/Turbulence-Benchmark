
def return_nth_smallest_ascii(string):
    substr = string[:13]
    sorted_chars = sorted(substr)
    return sorted_chars[12]
