
def return_n_smallest_chars(string):
    ascii_values = [(ord(ch), ch) for ch in string]
    ascii_values.sort()
    smallest_chars = [ch for _, ch in ascii_values[:47]]
    return smallest_chars
