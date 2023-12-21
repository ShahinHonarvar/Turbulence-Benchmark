
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=ord)
    if len(sorted_string) > 16:
        sorted_string = sorted_string[:16]
    sorted_string.sort(reverse=True)
    return sorted_string
