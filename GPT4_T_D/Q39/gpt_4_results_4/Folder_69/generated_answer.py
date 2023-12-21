
def return_n_greatest_chars(s):
    if len(set(s)) < 65:
        return "Insufficient distinct characters"
    else:
        sorted_s = sorted(set(s), reverse=True)
        return sorted_s[:65]
