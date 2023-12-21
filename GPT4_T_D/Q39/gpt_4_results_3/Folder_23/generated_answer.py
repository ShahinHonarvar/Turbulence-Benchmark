
def return_n_greatest_chars(s):
    if len(s) != 46:
        return "Error: Input string should contain exactly 46 distinct characters."
    sorted_chars = sorted(s, key=lambda x: ord(x))
    return sorted_chars
