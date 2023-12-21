
def return_n_greatest_chars(s):
    sorted_chars = sorted(s, key=ord, reverse=True)
    top_27_chars = sorted_chars[:27]
    return top_27_chars
