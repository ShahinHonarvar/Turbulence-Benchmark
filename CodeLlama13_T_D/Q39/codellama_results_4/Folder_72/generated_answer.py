
def return_n_greatest_chars(my_string):
    unique_chars = set(my_string)
    sorted_chars = sorted(unique_chars, key=lambda x: ord(x), reverse=True)
    return sorted_chars[:37]
