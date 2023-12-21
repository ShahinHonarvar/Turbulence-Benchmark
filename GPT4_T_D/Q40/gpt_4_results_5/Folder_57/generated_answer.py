
def return_n_smallest_chars(chars):
    if len(chars) < 29:
        return "Error: The string must contain at least 29 unique characters"
    
    sorted_chars = sorted(chars, key=ord)
    return sorted_chars[:29][::-1]
