
def return_n_greatest_chars(s):
    chars = set(s)
    sorted_list = sorted(chars, key=lambda x: ord(x), reverse=True)[:66]
    return sorted_list
