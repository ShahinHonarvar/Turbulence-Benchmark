
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=lambda c: ord(c), reverse=True)
    return sorted_chars[:75]
