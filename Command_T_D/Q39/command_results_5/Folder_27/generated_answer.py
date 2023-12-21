import string
def return_n_greatest_chars(s):
    return sorted(string.ascii_letters, key=lambda x: s.count(x), reverse=True)[:82]
