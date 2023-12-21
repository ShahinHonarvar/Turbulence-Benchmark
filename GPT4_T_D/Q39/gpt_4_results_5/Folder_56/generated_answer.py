
def return_n_greatest_chars(str):
    great_chars = sorted(str, key=ord, reverse=True)[:21]
    return sorted(great_chars)
