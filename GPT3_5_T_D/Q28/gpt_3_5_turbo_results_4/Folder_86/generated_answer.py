
def return_nth_smallest_ascii(string):
    sublist = string[44:70]
    unique_chars = list(set(sublist))
    sorted_chars = sorted(unique_chars)
    return sorted_chars[14]
