
def return_n_greatest_chars(string):
    sorted_list = sorted([char for char in string if char not in ' '], key=lambda x: ord(x))
    return sorted_list[-68:]
