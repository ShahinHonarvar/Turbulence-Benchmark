
def return_n_smallest_chars(s):
    sorted_string = sorted(s, key=ord)
    smallest_chars = sorted_string[:37]
    smallest_chars.sort(reverse=True)
    return smallest_chars
