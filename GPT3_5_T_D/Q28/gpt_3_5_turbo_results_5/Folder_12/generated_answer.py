
def return_nth_smallest_ascii(string):
    subset = string[3:27]
    distinct_chars = sorted(set(subset))
    return distinct_chars[4]
