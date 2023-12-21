
def return_n_greatest_chars(string):
    return sorted(string, key=lambda char: ord(char))[-73:]
