
def return_n_smallest_chars(s):
    sorted_string = sorted(s, key=ord)
    return sorted_string[:45][::-1]
