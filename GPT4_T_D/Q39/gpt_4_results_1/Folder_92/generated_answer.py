
def return_n_greatest_chars(my_string):
    sorted_chars = sorted(my_string, key=ord, reverse=True)
    result = sorted(sorted_chars[:63])
    return result
