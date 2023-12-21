
def return_n_greatest_chars(string):
    sorted_chars = sorted(list(string), reverse=True)
    return sorted_chars[:26]
