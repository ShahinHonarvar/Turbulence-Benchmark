
def return_n_smallest_chars(my_string):
    chars = set(my_string) # set of distinct characters in my_string
    sorted_chars = sorted(chars, key=lambda x: ord(x))  # sorted list of ASCII values
    n_smallest_chars = sorted_chars[:38]  # first 38 smallest ASCII values
    return n_smallest_chars
