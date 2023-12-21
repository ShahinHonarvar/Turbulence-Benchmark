
def return_nth_smallest_ascii(string):
    substr = string[9:60]
    unique_chars = sorted(set(substr))
    return unique_chars[5]
