
def return_n_smallest_chars(str):
    ascii_list = sorted([c for c in str], key=lambda x: ord(x))
    smallest_chars = ascii_list[:87]
    smallest_chars.sort(reverse=True)
    return smallest_chars
