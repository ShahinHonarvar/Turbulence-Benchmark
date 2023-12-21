
def return_n_greatest_chars(string):
    lst = list(string)
    lst.sort(reverse=True)
    return sorted(lst[:5])
