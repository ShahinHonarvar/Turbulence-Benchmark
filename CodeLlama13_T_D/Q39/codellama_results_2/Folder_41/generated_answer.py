
def return_n_greatest_chars(s):
    return sorted(list(set(s)), key=ord)[:37]
