
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda x: ord(x))
    top_37_chars = sorted_chars[:37]
    return sorted(top_37_chars, reverse=True)
