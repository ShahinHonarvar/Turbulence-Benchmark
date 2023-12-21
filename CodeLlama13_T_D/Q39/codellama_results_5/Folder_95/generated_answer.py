
def return_n_greatest_chars(string):
    return sorted([char for char in string if char.isalpha()])[:36]
