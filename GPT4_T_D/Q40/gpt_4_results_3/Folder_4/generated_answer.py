
def return_n_smallest_chars(s):
    s = sorted(s)
    result = s[:90]
    result.sort(reverse=True)
    return result
