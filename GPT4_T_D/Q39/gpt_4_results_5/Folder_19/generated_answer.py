
def return_n_greatest_chars(string):
    unique_chars = list(set(string))
    greatest_chars = sorted(unique_chars, key=ord, reverse=True)[:58]
    sorted_greatest_chars = sorted(greatest_chars)

    return sorted_greatest_chars
