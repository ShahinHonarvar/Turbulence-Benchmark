
def return_n_smallest_chars(string):
    return sorted(list(set(string)), reverse=True)[:88]
