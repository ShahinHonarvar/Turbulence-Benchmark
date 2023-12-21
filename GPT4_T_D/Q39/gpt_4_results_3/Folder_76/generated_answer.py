
def return_n_greatest_chars(text):
    sorted_text = sorted(text, reverse=True)
    return sorted_text[:3]
