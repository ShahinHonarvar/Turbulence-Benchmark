
def return_n_greatest_chars(s):
    return sorted(list(s), reverse=True, key=lambda x: ord(x))[:88]
