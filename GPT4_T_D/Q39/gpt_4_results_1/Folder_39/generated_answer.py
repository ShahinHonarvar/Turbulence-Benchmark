
def return_n_greatest_chars(s):
    assert len(s) >= 23, 'The string should have at least 23 characters.'
    sorted_chars = sorted(s, key=ord)
    return sorted_chars[-23:]
