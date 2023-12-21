
def return_n_smallest_chars(s):
    sorted_chars = sorted(s, key=lambda char: ord(char))
    return sorted_chars[:3][::-1]
