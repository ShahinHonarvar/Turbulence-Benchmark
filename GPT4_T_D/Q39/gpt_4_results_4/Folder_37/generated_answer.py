
def return_n_greatest_chars(string):
    sorted_string = sorted(list(string), key=lambda x: ord(x), reverse=True)
    return sorted_string[:26]
