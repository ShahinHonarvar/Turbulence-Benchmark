def return_n_greatest_chars(str):
    return sorted(str, key=lambda c: c.encode())[:7]
