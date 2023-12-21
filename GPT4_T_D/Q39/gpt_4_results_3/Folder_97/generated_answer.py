
def return_n_greatest_chars(chars):
    chars_list = sorted(list(set(chars)), key=ord, reverse=True)
    return sorted(chars_list[:38]) if len(chars_list) >= 38 else "Not enough distinct chars"
