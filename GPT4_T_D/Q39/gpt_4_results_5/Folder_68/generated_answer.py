
def return_n_greatest_chars(s):
    sorted_characters = sorted(s, key=lambda x: ord(x), reverse=True)
    greatest_89 = sorted_characters[:89]
    return greatest_89
