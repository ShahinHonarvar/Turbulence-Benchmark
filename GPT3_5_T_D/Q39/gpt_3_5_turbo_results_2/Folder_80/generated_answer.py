
def return_n_greatest_chars(string):
    sorted_list = sorted(string, reverse=True, key=lambda x: ord(x))
    return sorted_list[:35]
