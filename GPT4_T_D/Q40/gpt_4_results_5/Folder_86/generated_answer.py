
def return_n_smallest_chars(string):
    if len(string) <= 34:
        return sorted(list(string))
    else:
        return sorted(list(string))[:34]
