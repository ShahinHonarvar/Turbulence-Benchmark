
def return_n_smallest_chars(string):
    if len(string) <= 88:
        return sorted(string, reverse=True)
    else:
        return sorted(string)[:88][::-1]
