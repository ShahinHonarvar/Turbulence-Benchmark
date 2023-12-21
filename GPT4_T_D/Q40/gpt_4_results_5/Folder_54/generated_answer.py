
def return_n_smallest_chars(string):
    sorted_string = sorted(string, key=lambda char: ord(char))
    smallest_chars = sorted_string[:79]
    smallest_chars.sort(reverse=True)
    return smallest_chars
