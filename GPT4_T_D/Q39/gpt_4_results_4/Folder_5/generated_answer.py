
def return_n_greatest_chars(character_string):
    greatest_chars = sorted(character_string, reverse=True, key=ord)[:46]
    return greatest_chars
