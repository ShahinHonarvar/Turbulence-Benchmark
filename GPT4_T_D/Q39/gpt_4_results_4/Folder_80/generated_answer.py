
def return_n_greatest_chars(s):
    sorted_s = sorted(s, key=lambda x: ord(x), reverse=True)
    greatest_char = sorted_s[:35]
    greatest_char.sort()
    return greatest_char
