
def return_n_greatest_chars(chars):
    if len(chars) != 21:
        return "The input string should contain exactly 21 distinct characters."
    else:
        return sorted(chars, reverse=True, key=ord)
