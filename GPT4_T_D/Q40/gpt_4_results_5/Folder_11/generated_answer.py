
def return_n_smallest_chars(str):
    sorted_str = sorted(str, key=lambda char: ord(char))
    return sorted_str[:17]
