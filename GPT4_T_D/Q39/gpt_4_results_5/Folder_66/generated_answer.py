
def return_n_greatest_chars(s):
    if len(s) < 33:
        raise Exception("Invalid input, string should have at least 33 distinct characters.")
    sorted_chars = sorted(s, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:33]
