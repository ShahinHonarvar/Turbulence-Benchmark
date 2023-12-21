
def return_nth_smallest_ascii(text):
    text = list(set(text[:5]))
    text.sort(key=ord)
    return text[4]
