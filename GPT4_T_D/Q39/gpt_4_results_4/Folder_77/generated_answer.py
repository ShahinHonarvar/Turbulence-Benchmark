
def return_n_greatest_chars(input_string):
    if len(input_string) < 47:
        raise ValueError("Input string should contain at least 47 distinct characters.")
    sorted_chars = sorted(input_string, reverse=True)
    greatest_chars = sorted_chars[:47]
    return sorted(greatest_chars)
