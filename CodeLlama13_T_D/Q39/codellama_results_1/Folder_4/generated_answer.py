
def return_n_greatest_chars(string):
    return sorted([chr(i) for i in range(128)], key=lambda x: ord(x), reverse=True)[:90]
