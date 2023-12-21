
def return_n_greatest_chars(text):
    sorted_text = sorted(text, key=ord, reverse=True)
    return sorted_text[:57]
