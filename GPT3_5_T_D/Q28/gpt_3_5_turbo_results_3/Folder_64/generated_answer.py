
def return_nth_smallest_ascii(chars):
    if len(chars) < 7:
        return 'Input string is too short!'
    subset = sorted(chars[:7])
    return subset[6]
