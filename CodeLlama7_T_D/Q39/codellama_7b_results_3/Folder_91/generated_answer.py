
def return_n_greatest_chars(string, n=6):
    if len(string) < n:
        raise ValueError("String is shorter than N")
    greatest_chars = sorted(string, key=ord, reverse=True)[:n]
    return greatest_chars
