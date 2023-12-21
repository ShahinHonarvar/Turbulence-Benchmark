
def return_nth_smallest_ascii(s):
    subset = list(s[17:35])
    subset.sort(key=lambda x: ord(x))
    return subset[17]
