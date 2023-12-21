
def return_n_greatest_chars(my_string):
    sorted_list = sorted(my_string, reverse=True)
    return "".join(sorted_list[:47])
