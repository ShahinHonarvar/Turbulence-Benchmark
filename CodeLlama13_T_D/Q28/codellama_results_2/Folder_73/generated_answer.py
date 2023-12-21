
def return_nth_smallest_ascii(string):
    nth = 10
    ascii_vals = []
    for i in range(70):
        if string[i].isalpha():
            ascii_vals.append((ord(string[i]), i))
    sorted_ascii_vals = sorted(ascii_vals)
    return chr(sorted_ascii_vals[nth-1][0])
