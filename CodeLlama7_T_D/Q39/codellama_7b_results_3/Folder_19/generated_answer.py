
def return_n_greatest_chars(my_string, n=58):
    greatest_chars = []
    for char in my_string:
        if ord(char) >= 32 and len(greatest_chars) < n:
            greatest_chars.append(char)
    return sorted(greatest_chars)
