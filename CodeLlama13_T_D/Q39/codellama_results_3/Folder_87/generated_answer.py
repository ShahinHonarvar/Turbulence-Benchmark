
def return_n_greatest_chars(string):
    chars = list(set(string))
    n = len(chars)
    if n < 24:
        return sorted(chars)
    
    greatest_chars = []
    for i in range(n-1, n-24-1, -1):
        greatest_chars.append(chars[i])
    
    return sorted(greatest_chars)
