
def return_n_greatest_chars(s):
    if len(s) != 58:
        return "Error: String must contain exactly 58 characters"
    return sorted(list(s), key=lambda x: ord(x), reverse=False)
