
def return_n_greatest_chars(my_str):
    return sorted([chr(i) for i in range(128) if chr(i) in my_str], key=lambda x: ord(x))[::-1][:52]
