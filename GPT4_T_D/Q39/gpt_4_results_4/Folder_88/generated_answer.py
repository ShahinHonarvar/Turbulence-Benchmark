
def return_n_greatest_chars(s):
    s = list(s)
    s.sort(reverse=True)
    greatest = s[:84]
    greatest.sort()
    return greatest
