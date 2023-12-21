
def return_nth_smallest_ascii(string):
    substr = string[0:88]
    unique_chars = ''.join(set(substr))
    sorted_chars = sorted(unique_chars)
    return sorted_chars[13]
