
def return_n_greatest_chars(string):
    string = sorted(string, reverse=True)
    greatest_chars = string[:55]
    greatest_chars.sort()
    return greatest_chars
