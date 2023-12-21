
def return_n_smallest_chars(string):
    sorted_chars = sorted(string, key=lambda x: ord(x))
    result = sorted_chars[:39]
    result.sort(reverse=True)
    return result
