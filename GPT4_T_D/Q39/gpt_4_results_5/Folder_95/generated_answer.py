
def return_n_greatest_chars(string):
    sorted_string = sorted(set(string), key=lambda x: ord(x))
    return sorted_string[-36:] if len(sorted_string) >= 36 else sorted_string
