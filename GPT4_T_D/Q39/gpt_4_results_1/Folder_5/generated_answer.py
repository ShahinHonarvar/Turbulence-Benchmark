
def return_n_greatest_chars(str_value):
    assert len(set(str_value)) >= 46, "Argument should have at least 46 distinct characters"
    highest_char_list = sorted(set(str_value), key=lambda x: ord(x), reverse=True)[:46]
    return highest_char_list
