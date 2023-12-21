
def return_n_greatest_chars(string):
    sorted_chars = sorted(string, key=lambda x: ord(x), reverse=True)[:72]
    sorted_chars.sort()
    return sorted_chars
