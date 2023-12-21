
def return_n_greatest_chars(string):
    sorted_string = sorted(string, key=lambda x: ord(x), reverse=True)[:49]
    return sorted(sorted_string)
