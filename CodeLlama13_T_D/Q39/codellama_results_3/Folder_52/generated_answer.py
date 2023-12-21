
def return_n_greatest_chars(s):
    return sorted([chr(i) for i in range(128) if chr(i) in s], reverse=True)[:68]
