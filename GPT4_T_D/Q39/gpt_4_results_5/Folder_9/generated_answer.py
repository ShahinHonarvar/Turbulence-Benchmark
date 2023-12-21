
def return_n_greatest_chars(given_string):
    sorted_string = list(given_string)
    sorted_string.sort(key=lambda char: ord(char), reverse=True)
    greatest_chars = sorted_string[:20]
    greatest_chars.sort()
    return greatest_chars
