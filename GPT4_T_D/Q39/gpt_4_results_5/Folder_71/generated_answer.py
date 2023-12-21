
def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x), reverse=True)
    greatest_chars = sorted_s[:14]
    return sorted(greatest_chars)
