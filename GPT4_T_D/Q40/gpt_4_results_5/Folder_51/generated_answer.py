
def return_n_smallest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x), reverse=True)
    return sorted_s[:45]
