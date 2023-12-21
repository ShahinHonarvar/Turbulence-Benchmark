def return_n_greatest_chars(str):
    res = [char for char in str if char.isalpha()]
    return res[:63]
