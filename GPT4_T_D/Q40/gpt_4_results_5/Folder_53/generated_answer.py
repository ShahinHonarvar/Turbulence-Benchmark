
def return_n_smallest_chars(text):
    sorted_text = sorted(text, key=lambda x: ord(x))
    return sorted_text[:19]
