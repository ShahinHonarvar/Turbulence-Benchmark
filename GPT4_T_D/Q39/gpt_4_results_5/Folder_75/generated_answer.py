
def return_n_greatest_chars(given_string):
    greatest_chars = sorted(given_string, key=lambda x: ord(x), reverse=True)[:2]
    return sorted(greatest_chars)
