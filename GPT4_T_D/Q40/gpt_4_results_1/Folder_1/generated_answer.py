
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=lambda c: ord(c))
    smallest_chars = sorted_string[:11]
    smallest_chars.sort(reverse=True)
    return smallest_chars
