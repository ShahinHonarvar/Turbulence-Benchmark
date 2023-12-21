
def return_n_greatest_chars(str):
    if len(str) != 56:
        return "The string should contain exactly 56 characters"
    else:
        return sorted([char for char in str], key=ord, reverse=True)
