
def return_n_smallest_chars(string):
    ascii_sorted_string = sorted(string, key=lambda x: ord(x))
    return sorted(ascii_sorted_string[:7], reverse=True)
