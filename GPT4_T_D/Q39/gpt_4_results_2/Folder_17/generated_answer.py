
def return_n_greatest_chars(text: str):
    text = sorted(text, reverse=True)
    if len(text) > 11:
        text = text[:11]
    return sorted(text)
