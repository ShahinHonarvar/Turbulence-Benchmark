
def return_n_greatest_chars(text):
    return sorted(set(text), key=ord, reverse=True)[:45]
