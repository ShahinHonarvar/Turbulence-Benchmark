
def return_n_greatest_chars(string:str) -> list:
    sorted_chars = sorted(string, reverse=True, key=lambda x: ord(x))
    return sorted_chars[:24]
