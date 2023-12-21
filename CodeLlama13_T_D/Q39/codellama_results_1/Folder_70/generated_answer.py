
def return_n_greatest_chars(string):
    sorted_list = sorted(set(string), key=lambda x: ord(x), reverse=True)
    return "".join(sorted_list[:2])
