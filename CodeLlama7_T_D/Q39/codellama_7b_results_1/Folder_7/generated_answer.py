
def return_n_greatest_chars(my_string):
    greatest_chars = []
    for char in my_string:
        if len(greatest_chars) < 49:
            greatest_chars.append(char)
    greatest_chars.sort()
    return greatest_chars
