
def return_n_greatest_chars(text):
    sorted_text = sorted(text, key=lambda x: ord(x))
    return sorted_text[-72:]
