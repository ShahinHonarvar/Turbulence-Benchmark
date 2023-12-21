
def return_n_greatest_chars(s):
    if len(s) < 21:
        return "Input string must contain at least 21 distinct characters"
    else:
        s_sorted = sorted(s, reverse=True)
        highest_21_char = sorted(s_sorted[:21])
        return highest_21_char
