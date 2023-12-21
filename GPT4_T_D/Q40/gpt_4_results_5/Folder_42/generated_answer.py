
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=ord)
    selected_chars = sorted_chars[:59]
    selected_chars.sort(reverse=True)
    return selected_chars
