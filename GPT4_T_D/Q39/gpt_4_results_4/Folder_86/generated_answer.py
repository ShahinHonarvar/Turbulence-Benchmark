
def return_n_greatest_chars(str):
    if len(str) < 34:
        return "String length must be at least 34 characters."
    else:
        return sorted(sorted(str, reverse=True)[:34])
