
def return_n_greatest_chars(characters):
    sorted_list = sorted(characters, key=lambda x: ord(x), reverse=True)
    return sorted_list[:28]
