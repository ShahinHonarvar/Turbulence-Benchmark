
def return_n_greatest_chars(my_str):
    return sorted([char for char in my_str if char.isalpha()], key=lambda x: ord(x), reverse=True)[:8]
