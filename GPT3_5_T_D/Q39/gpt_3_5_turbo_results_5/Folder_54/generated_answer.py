
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, reverse=True, key=lambda x: ord(x))
    return sorted_chars[:79]
