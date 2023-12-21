
def return_n_smallest_chars(chars):
    
    sorted_chars = sorted(chars, key=ord)
    top_chars = sorted_chars[:90]

    return sorted(top_chars, reverse=True)
