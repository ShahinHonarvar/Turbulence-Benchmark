
def return_n_smallest_chars(string):
    return sorted([char for char in string if char.isalpha()], key=ord)[:7]
