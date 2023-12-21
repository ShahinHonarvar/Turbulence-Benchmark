
def return_n_smallest_chars(s):
    s = sorted(s)
    result = s[:44]
    result.sort(reverse=True)
    return result
