
def return_n_smallest_chars(s):
    if len(s) < 32:
        return []
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return sorted_chars[:32][::-1]
