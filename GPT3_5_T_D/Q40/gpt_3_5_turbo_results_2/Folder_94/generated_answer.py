
def return_n_smallest_chars(string):
    result = sorted(string)[:87]
    return sorted(result, reverse=True)
