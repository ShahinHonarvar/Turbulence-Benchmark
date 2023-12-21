
def return_nth_smallest_ascii(string):
    subset = string[:11]
    sorted_chars = sorted(subset)
    return sorted_chars[10]
